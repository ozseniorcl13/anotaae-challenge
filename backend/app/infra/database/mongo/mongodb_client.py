from motor.motor_asyncio import AsyncIOMotorClient

from app.infra.config.config import config


class MongoDBClient:
    def __init__(self):
        self.client = AsyncIOMotorClient(config.DB_URL)
        self.db = self.client[config.DB_NAME]

    def get_collection(self, name: str):
        return self.db[name]
