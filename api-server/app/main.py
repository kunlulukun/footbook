from fastapi import FastAPI
from starlette.exceptions import HTTPException

from app.routers import student, login, user
from app.server.api_logger_middleware import APILoggerMiddleware
from app.server.http_exception_handler import http_exception_handler

app = FastAPI(
    docs_url="/swagger",

)

app.include_router(student.router)
app.include_router(login.router)
app.include_router(user.router)

app.add_middleware(APILoggerMiddleware)

app.add_exception_handler(HTTPException, http_exception_handler)

