from typing import Optional

from bson import ObjectId

from app.storages.student.models import StudentModel
from app.storages.student.mongo_config import students_collection


async def create_student(student: StudentModel) -> Optional[StudentModel]:
    result = await students_collection.insert_one(student.model_dump(by_alias=True, exclude={"id"}))
    if not result.acknowledged:
        return None
    student.id = result.inserted_id
    return student


async def get_student(student_id: str) -> Optional[StudentModel]:
    if not ObjectId.is_valid(student_id):
        return None
    doc = await students_collection.find_one(
        filter={"_id": ObjectId(student_id)}
    )
    if doc is None:
        return None
    return StudentModel(**doc)


async def update_student(student_id: str, student_update: StudentModel) -> int:
    result = await students_collection.update_one(
        filter={"_id": ObjectId(student_id)},
        update={"$set": student_update.model_dump(by_alias=True, exclude={"id"})}
    )
    return result.matched_count


async def delete_student(student_id: str) -> int:
    result = await students_collection.delete_one(
        filter={"_id": ObjectId(student_id)}
    )
    return result.deleted_count
