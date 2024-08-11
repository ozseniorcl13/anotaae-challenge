from abc import ABC, abstractmethod

from app.domain.category.model.category import Category


class CategoryRepository(ABC):

    @abstractmethod
    async def create(self, category: Category) -> Category:
        pass
