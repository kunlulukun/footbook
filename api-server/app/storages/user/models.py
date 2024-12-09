from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class UserModel(BaseModel):
    id: str
    display_name: str
    email: str
    address: Optional[str] = Field(default=None)
    tel: Optional[str] = Field(default=None)
    password: Optional[str] = Field(default=None)  # only used for login
    created_at: Optional[datetime] = Field(default=None)
    updated_at: Optional[datetime] = Field(default=None)
