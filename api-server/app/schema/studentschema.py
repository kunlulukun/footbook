from typing import Optional

from pydantic import BaseModel, Field


class StudentSchema(BaseModel):
    id: Optional[str] = Field(None)
    name: str
    age: int
    class_name: str
