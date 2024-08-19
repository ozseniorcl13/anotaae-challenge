from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient

from app.domain.product.model.product import Product
from app.domain.product.repository.product_repository import ProductRepository


class ProductRepositoryImpl(ProductRepository):
    def __init__(self, db_client: AsyncIOMotorClient):
        self.collection = db_client.get_collection("products")

    async def create(self, product: Product) -> Product:
        product_created = await self.collection.insert_one(product.dict())

        print("*************")
        print(product_created.inserted_id)
        product_id = str(product_created.inserted_id)

        product = await self.get_by_id(product_id)

        print("**************************")
        print(product)

        return Product.format_from_create(product.dict(), product_id)

    async def get_by_id(self, id: str) -> Product:
        result = await self.collection.aggregate(
            [
                {"$match": {"_id": ObjectId(id)}},
                {
                    "$lookup": {
                        "from": "categories",
                        "localField": "_id",
                        "foreignField": "category_id",
                        "as": "category",
                    }
                },
                {"$unwind": "$category"},
            ]
        ).to_list(1)

        print("****** result")
        print(result)

        if not result:
            return None

        product_data = result[0]

        return Product(**product_data)
