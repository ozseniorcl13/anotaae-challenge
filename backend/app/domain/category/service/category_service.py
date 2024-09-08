from typing import List

from bson import ObjectId

from app.application.api.category.dto.category_request import (
    CategoryCreateDTO, CategoryUpdateDTO)
from app.application.api.category.dto.category_response import \
    CategoryResponseDTO
from app.domain.category.entity.category import Category
from app.domain.category.exception.category_exception import (
    CategoryNotFoundException, InvalidIdException)
from app.domain.category.repository.category_repository import \
    CategoryRepository


class CategoryService:
    def __init__(self, category_repository: CategoryRepository):
        self.category_repository = category_repository

    async def create(self, category_data: CategoryCreateDTO) -> CategoryResponseDTO:
        category = Category(**category_data.dict())
        created_category = await self.category_repository.create(category)
        return CategoryResponseDTO(**created_category.dict())

    async def get_all(self) -> List[CategoryResponseDTO]:
        categories = await self.category_repository.get_all()
        return [CategoryResponseDTO(**category.dict()) for category in categories]

    async def get_by_id(self, id: str) -> CategoryResponseDTO:
        if not ObjectId.is_valid(id):
            raise InvalidIdException(id)

        category = await self.category_repository.get_by_id(id)
        if not category:
            raise CategoryNotFoundException(id)
        return CategoryResponseDTO(**category.dict())

    async def update(
        self, id: str, category_data: CategoryUpdateDTO
    ) -> CategoryResponseDTO:
        if not ObjectId.is_valid(id):
            raise InvalidIdException(id)

        category = await self.category_repository.get_by_id(id)
        if not category:
            raise CategoryNotFoundException(id)

        category.update_values(category_data.dict(exclude_unset=True))
        updated_category = await self.category_repository.update(id, category)

        return CategoryResponseDTO(**updated_category.dict())

    async def delete(self, id: str):
        if not ObjectId.is_valid(id):
            raise InvalidIdException(id)

        category = await self.category_repository.get_by_id(id)
        if not category:
            raise CategoryNotFoundException(id)

        await self.category_repository.delete(id)
