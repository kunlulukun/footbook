import os


class Config:
    MONGO_URI = os.getenv("MONGO_URI")
    MYSQL_HOST = os.getenv("MYSQL_HOST")
    MYSQL_PORT = os.getenv("MYSQL_PORT")
    MYSQL_USER = os.getenv("MYSQL_USER")
    MYSQL_PWD = os.getenv("MYSQL_PWD")
    MYSQL_DB = os.getenv("MYSQL_DB")
