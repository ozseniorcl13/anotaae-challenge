from abc import ABC, abstractmethod
from typing import List

from app.domain.category.model.category import Category


class CategoryRepository(ABC):

    @abstractmethod
    async def create(self, category: Category) -> Category:
        pass

    @abstractmethod
    async def get_by_id(self, id: str) -> Category:
        pass

    @abstractmethod
    async def get_all(self) -> List[Category]:
        pass

    @abstractmethod
    async def delete(self, id: str):
        pass

    @abstractmethod
    async def update(self, category_id: str, category: Category) -> Category:
        pass
