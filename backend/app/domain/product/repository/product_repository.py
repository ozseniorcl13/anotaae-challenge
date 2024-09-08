from abc import ABC, abstractmethod
from typing import List

from app.domain.product.entity.product import Product


class ProductRepository(ABC):

    @abstractmethod
    async def create(self, product: Product) -> Product:
        pass

    @abstractmethod
    async def get_all(self) -> List[Product]:
        pass

    @abstractmethod
    async def get_by_id(self, id: str) -> Product:
        pass

    @abstractmethod
    async def update(self, id: str, product: Product) -> Product:
        pass

    @abstractmethod
    async def delete(self, id: str):
        pass
