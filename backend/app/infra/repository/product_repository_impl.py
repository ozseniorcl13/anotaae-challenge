from motor.motor_asyncio import AsyncIOMotorClient

from app.domain.product.model.product import Product
from app.domain.product.repository.product_repository import ProductRepository


class ProductRepositoryImpl(ProductRepository):
    def __init__(self, db_client: AsyncIOMotorClient):
        self.collection = db_client.get_collection("products")

    async def create(self, product: Product) -> Product:
        result = await self.collection.insert_one(product.dict())
        product.id = str(result.inserted_id)
        return product
