from motor.motor_asyncio import AsyncIOMotorClient

from app.domain.category.model.category import Category
from app.domain.category.repository.category_repository import CategoryRepository


class CategoryRepositoryImpl(CategoryRepository):
    def __init__(self, db_client: AsyncIOMotorClient):
        self.collection = db_client.get_collection("categories")

    async def create(self, category: Category) -> Category:
        result = await self.collection.insert_one(category.dict())
        category.id = str(result.inserted_id)
        return category
