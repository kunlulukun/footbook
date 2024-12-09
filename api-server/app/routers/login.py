from fastapi import APIRouter

from app.schema.loginschema import LoginRequestSchema, LoginResponseSchema, SigninResponseSchema, SigninRequestSchema
from app.service import user_service

router = APIRouter(prefix="/login", tags=["login"])


@router.post("/signin", response_model=SigninResponseSchema)
async def signin(signin_request: SigninRequestSchema):
    print(f"{signin_request}")
    return await user_service.signin(signin_request)


@router.post("/", response_model=LoginResponseSchema)
async def login(login_request: LoginRequestSchema):
    print(f"{login_request}")
    return await user_service.login(login_request)
