from typing import List

from app.domain.product.entity.product import Product
from app.infra.database.mongo.document.product_document import ProductDocument


class ProductRepositoryImpl:

    async def create(self, product: Product) -> Product:
        product_doc = ProductDocument(**product.dict())
        await product_doc.insert()
        return Product(**product_doc.dict())

    async def get_all(self) -> List[Product]:
        products = await ProductDocument.find_all().to_list()
        return [Product(**product.dict()) for product in products]

    async def get_by_id(self, id: str) -> Product:
        product_doc = await ProductDocument.get(id)
        if product_doc:
            return Product(**product_doc.dict())
        return None

    async def update(self, id: str, product: Product) -> Product:
        product_doc = await ProductDocument.get(id)
        await product_doc.set(product.dict())
        return Product(**product_doc.dict())

    async def delete(self, id: str):
        product_doc = await ProductDocument.get(id)
        await product_doc.delete()
