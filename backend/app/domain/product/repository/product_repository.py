from abc import ABC, abstractmethod

from app.domain.product.model.product import Product


class ProductRepository(ABC):

    @abstractmethod
    async def create(self, product: Product) -> Product:
        pass

    @abstractmethod
    async def get_by_id(self, id: str) -> Product:
        pass
