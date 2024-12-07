from fastapi import FastAPI
from app.routers import student, login, user

app = FastAPI(
    docs_url="/swagger",

)

app.include_router(student.router)
app.include_router(login.router)
app.include_router(user.router)
