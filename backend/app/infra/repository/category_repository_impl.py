from typing import List
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient

from app.domain.category.model.category import Category
from app.domain.category.repository.category_repository import CategoryRepository


class CategoryRepositoryImpl(CategoryRepository):
    def __init__(self, db_client: AsyncIOMotorClient):
        self.collection = db_client.get_collection("categories")

    async def create(self, category: Category) -> Category:
        result = await self.collection.insert_one(category.dict())
        return Category.format_from_create(category.dict(), result.inserted_id)

    async def get_by_id(self, category_id: str) -> Category:
        result = await self.collection.find_one({"_id": ObjectId(category_id)})
        if result:
            return Category.format_from_get(result)
        return None

    async def get_all(self) -> List[Category]:
        results = await self.collection.find().to_list(length=100)
        return [Category.format_from_get(result) for result in results]

    async def delete(self, category_id: str):
        result = await self.collection.delete_one({"_id": ObjectId(category_id)})
        return result

    async def update(self, category_id: str, category: Category) -> Category:
        await self.collection.update_one(
            {"_id": ObjectId(category_id)}, {"$set": category.dict()}
        )
        return Category.format_from_create(category.dict(), category_id)
