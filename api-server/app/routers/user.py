from fastapi import APIRouter

from app.schema.userschema import UpdateUserinfoRequestSchema, UpdateUserinfoResponseSchema, GetUserinfoResponseSchema

router = APIRouter(prefix="/userinfo", tags=["userinfo"])


@router.post("/", response_model=UpdateUserinfoResponseSchema)
async def update_user(userinfo_request: UpdateUserinfoRequestSchema):
    print(f"{userinfo_request}")
    return UpdateUserinfoResponseSchema(success=True)


@router.get("/{user_id}", response_model=GetUserinfoResponseSchema)
async def get_user(user_id: str):
    return GetUserinfoResponseSchema(display_name="lulu", tel="23", address="tutu")

