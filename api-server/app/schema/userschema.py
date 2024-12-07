from pydantic import BaseModel


class UpdateUserinfoRequestSchema(BaseModel):
    display_name: str
    tel: str
    address:str

class UpdateUserinfoResponseSchema(BaseModel):
    success: bool


class GetUserinfoRequestSchema(BaseModel):
    user_id: str

class GetUserinfoResponseSchema(BaseModel):
    display_name: str
    tel: str
    address: str