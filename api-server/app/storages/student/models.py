from typing import Optional

from pydantic import BaseModel, Field
from bson import ObjectId

from app.schema.studentschema import StudentSchema


class StudentModel(BaseModel):
    id: Optional[ObjectId] = Field(None, alias="_id", serialization_alias='_id')
    name: str
    age: int
    class_name: str

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

    @classmethod
    def from_api_schema(cls, student: StudentSchema):
        """
        Converts an API schema `Student` to `StudentModel`.
        """
        return StudentModel(
            id=None if student.id is None or not ObjectId.is_valid(student.id) else ObjectId(student.id),
            name=student.name,
            age=student.age,
            class_name=student.class_name
        )

    def to_api_schema(self) -> StudentSchema:
        """
        Converts `StudentModel` back to an API schema `Student`.
        """
        return StudentSchema(
            id=self.id.__str__(),
            name=self.name,
            age=self.age,
            class_name=self.class_name
        )
