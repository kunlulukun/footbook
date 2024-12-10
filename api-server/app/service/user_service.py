import hashlib
import uuid

from fastapi import HTTPException

from app.schema.loginschema import SigninRequestSchema, SigninResponseSchema, LoginRequestSchema, LoginResponseSchema
from app.storages.user.models import UserModel
import app.storages.user.storage as user_storage


async def signin(signin_request: SigninRequestSchema) -> SigninResponseSchema:

    # 1. 根据request插入记录到数据库
    # 1.1 ID要用一个UUID，需要生成UUID的方法
    # 1.2 密码要加密存储，需要用SHA-256加密request里的密码。

    # 2. 如果插入成功，返回True。 如果失败，返回False，让用户重试。
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
    # Create a sha256 hash object
    sha256 = hashlib.sha256()

    # Update the object with the password (encoded to bytes)
    sha256.update(password.encode('utf-8'))

    # Get the hexadecimal representation of the hash
    hashed_password = sha256.hexdigest()

    return hashed_password


async def login(login_request: LoginRequestSchema) -> LoginResponseSchema:

    # 1. 查询数据库，拿到id和pwd

    # 2. 如果没有结果，就是用户不存在。如果pwd不匹配，就是密码错误

    # 2.1 pwd是加密存储的，所以，查询的时候也要先加密request里的pwd然后再匹配

    # 3. 登录成功，需要返回token和id
    # 3.1 token是JWT，需要一个生成jwt的方法。
    model = await user_storage.select_user_for_login(login_request.e_mail)

    if model is None:
        raise HTTPException(status_code=404, detail="User not found.")

    if _hash_password(login_request.password) != model.password:
        raise HTTPException(status_code=401, detail="Incorrect password.")
    return LoginResponseSchema(token="123", user_id=model.id)