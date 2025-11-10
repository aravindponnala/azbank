import os
from motor.motor_asyncio import AsyncIOMotorClient


MONGO_URL = os.environ.get("MONGO_URL", "mongodb://localhost:27017")
DB_NAME = os.environ.get("MONGO_DB", "payments_db")


client = AsyncIOMotorClient(MONGO_URL)
db = client[DB_NAME]
