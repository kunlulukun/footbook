import os
from contextlib import contextmanager

import pymysql
from dbutils.pooled_db import PooledDB
from motor.motor_asyncio import AsyncIOMotorClient
from pymysql.cursors import DictCursor


class Config:
    MONGO_URI = os.getenv("MONGO_URI")
    MYSQL_HOST = os.getenv("MYSQL_HOST")
    MYSQL_PORT = os.getenv("MYSQL_PORT")
    MYSQL_USER = os.getenv("MYSQL_USER")
    MYSQL_PWD = os.getenv("MYSQL_PWD")
    MYSQL_DB = os.getenv("MYSQL_DB")


class SQLExecutor:
    def __init__(self, host, port, user, password, database, maxconnections=5, mincached=2):
        self.pool = PooledDB(
            creator=pymysql,
            maxconnections=maxconnections,
            mincached=mincached,
            blocking=True,
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
        )

    @contextmanager
    def get_connection(self):
        connection = self.pool.connection()
        try:
            yield connection
        finally:
            connection.close()

    def execute_query(self, query, params=None, commit=False, as_dict=False):
        """Execute a query, optionally commit and return results."""
        with self.get_connection() as connection:
            with connection.cursor(DictCursor if as_dict else None) as cursor:
                cursor.execute(query, params)
                if commit:
                    connection.commit()
                return cursor.fetchall()

mongo_client = AsyncIOMotorClient(Config.MONGO_URI)

mysql_executor = SQLExecutor(
    host=Config.MYSQL_HOST,
    port=int(Config.MYSQL_PORT),
    user=Config.MYSQL_USER,
    password=Config.MYSQL_PWD,
    database=Config.MYSQL_DB
)
