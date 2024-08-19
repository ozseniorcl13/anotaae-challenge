from app.domain.product.model.product import Product
from app.domain.product.repository.product_repository import ProductRepository
from app.domain.category.repository.category_repository import (
    CategoryRepository,
)


class ProductService:
    def __init__(
        self,
        product_repository: ProductRepository,
        category_repository: CategoryRepository,
    ):
        self.product_repository = product_repository
        self.category_repository = category_repository

    async def create_product(self, product_data: dict) -> Product:
        await self.category_repository.get_by_id(product_data["category_id"])
        product = Product(**product_data)
        return await self.product_repository.create(product)
