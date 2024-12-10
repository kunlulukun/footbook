from pydantic import BaseModel, Field


class LoginRequestSchema(BaseModel):
    e_mail: str
    password: str


class LoginResponseSchema(BaseModel):
    token: str
    user_id: str


class SigninRequestSchema(BaseModel):
    e_mail: str
    display_name:str
    password: str


class SigninResponseSchema(BaseModel):
    success: bool


