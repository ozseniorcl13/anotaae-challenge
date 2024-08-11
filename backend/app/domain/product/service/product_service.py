from app.domain.product.model.product import Product
from app.domain.product.repository.product_repository import ProductRepository


class ProductService:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    async def create_product(self, product_data: dict) -> Product:
        product = Product(**product_data)
        return await self.product_repository.create(product)
