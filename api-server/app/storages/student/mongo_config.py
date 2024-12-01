from motor.motor_asyncio import AsyncIOMotorClient
from app.config import Config

client = AsyncIOMotorClient(Config.MONGO_URI)
db = client["school"]
students_collection = db["students"]