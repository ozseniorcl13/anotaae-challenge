from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from app.infra.config.config import config
from app.infra.database.mongo.document.category_document import \
    CategoryDocument


class MongoDBClient:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MongoDBClient, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "client"):
            self.client = AsyncIOMotorClient(config.DB_URL)
            self.db = self.client[config.DB_NAME]

    async def init(self):
        await init_beanie(database=self.db, document_models=[CategoryDocument])

    async def get_db(self):
        return self.db

    async def close(self):
        if self.client:
            self.client.close()
