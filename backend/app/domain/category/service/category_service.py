from typing import List
from app.domain.category.model.category import Category
from app.domain.category.repository.category_repository import CategoryRepository
from app.domain.category.exception.category_exception import CategoryNotFoundException


class CategoryService:
    def __init__(self, category_repository: CategoryRepository):
        self.category_repository = category_repository

    async def create_category(self, category_data: dict) -> Category:
        category = Category(**category_data)
        return await self.category_repository.create(category)

    async def get_category_by_id(self, category_id: str) -> Category:
        category = await self.category_repository.get_by_id(category_id)

        if not category:
            raise CategoryNotFoundException(category_id)
        return category

    async def get_all_categories(self) -> List[Category]:
        categories = await self.category_repository.get_all()
        return categories

    async def delete_category(self, category_id: str):
        category = await self.get_category_by_id(category_id)
        await self.category_repository.delete(category_id)
        return category

    async def update_category(self, category_id: str, category_data: dict):
        await self.get_category_by_id(category_id)
        updated_category = Category(**category_data)
        result = await self.category_repository.update(category_id, updated_category)
        return result
