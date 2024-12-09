from typing import Optional

from app.config import mysql_executor
from app.storages.user.models import UserModel


async def insert_user(user_model: UserModel):
    query = "INSERT INTO users (id, display_name, email, password) VALUES (%s, %s, %s, %s)"
    try:
        result = mysql_executor.execute_query(
            query=query,
            params=(user_model.id, user_model.display_name, user_model.email, user_model.password),
            commit=True
        )
        return True
    except Exception as e:
        print(f"Error inserting user: {e}")
        return False


async def select_user_for_login(email:str) -> Optional[UserModel]:
    query = "SELECT * FROM users WHERE email = %s"
    result = mysql_executor.execute_query(
        query=query,
        params=(email,),
        commit=True,
        as_dict=True
    )

    if len(result) == 0:
        return None
    return UserModel(**result[0])