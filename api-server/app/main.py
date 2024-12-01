from fastapi import FastAPI
from app.routers import student

app = FastAPI(
    docs_url="/swagger",

)

app.include_router(student.router)
