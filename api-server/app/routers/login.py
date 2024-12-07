from fastapi import APIRouter

from app.schema.loginschema import LoginRequestSchema, LoginResponseSchema, SigninResponseSchema, SigninRequestSchema

router = APIRouter(prefix="/login", tags=["login"])


@router.post("/", response_model=LoginResponseSchema)
async def login(login_request: LoginRequestSchema):
    print(f"{login_request}")
    return LoginResponseSchema(token="nidetoken", user_id="niyeye")

@router.post("/signin", response_model=SigninResponseSchema)
async def signin(signin_request: SigninRequestSchema):
    print(f"{signin_request}")
    return SigninResponseSchema(success=True)