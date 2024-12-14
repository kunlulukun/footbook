import hashlib
import uuid

from fastapi import HTTPException

from app.schema.loginschema import SigninRequestSchema, SigninResponseSchema, LoginRequestSchema, LoginResponseSchema
from app.storages.user.models import UserModel
import app.storages.user.storage as user_storage
from app.service.jwt_helper import JWTHelper


async def signin(signin_request: SigninRequestSchema) -> SigninResponseSchema:
    generated_id = str(uuid.uuid4())
    hashed_pwd = _hash_password(signin_request.password)
    user_model = UserModel(
        id=generated_id,
        display_name=signin_request.display_name,
        email=signin_request.e_mail,
        password=hashed_pwd
    )
    success = await user_storage.insert_user(user_model)
    return SigninResponseSchema(success=success)


def _hash_password(password: str) -> str:
    sha256 = hashlib.sha256()

    sha256.update(password.encode('utf-8'))

    hashed_password = sha256.hexdigest()

    return hashed_password


async def login(login_request: LoginRequestSchema) -> LoginResponseSchema:
    model = await user_storage.select_user_for_login(login_request.e_mail)

    if model is None:
        raise HTTPException(status_code=404, detail="User not found.")

    if _hash_password(login_request.password) != model.password:
        raise HTTPException(status_code=401, detail="Incorrect password.")

    payload = {"user_id":model.id}
    token = JWTHelper.generate_jwt(payload,expiration_days = 90)
    return LoginResponseSchema(token=token, user_id=model.id)