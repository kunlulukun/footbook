from fastapi import APIRouter, HTTPException

from app.schema.studentschema import StudentSchema
from app.storages.student.models import StudentModel
from app.storages.student import storage as student_storage

router = APIRouter(prefix="/students", tags=["students"])


@router.post("/", response_model=StudentSchema)
async def create_student(student: StudentSchema):
    created_student = await student_storage.create_student(StudentModel.from_api_schema(student=student))
    return created_student.to_api_schema()


@router.get("/{student_id}", response_model=StudentSchema)
async def get_student(student_id: str):
    student = await student_storage.get_student(student_id=student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student.to_api_schema()


@router.put("/{student_id}", response_model=StudentSchema)
async def update_student(student_id: str, student_update: StudentSchema):
    updated_count = await student_storage.update_student(student_id=student_id,
                                                         student_update=StudentModel.from_api_schema(student_update))
    if not updated_count:
        raise HTTPException(status_code=404, detail="Student not found")
    return await get_student(student_id=student_id)


@router.delete("/{student_id}")
async def delete_student(student_id: str):
    deleted_count = await student_storage.delete_student(student_id=student_id)
    if not deleted_count:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted"}
