from bson import ObjectId
from pydantic import BaseModel


class Product(BaseModel):
    title: str
    description: str
    price: float
    category_id: str
    owner_id: str

    @classmethod
    def format_from_create(cls, product: dict, id: ObjectId) -> dict:
        return {
            "id": str(id),
            "title": product["title"],
            "description": product["description"],
            "price": product["price"],
            "category": product["category"],
            "owner_id": product["owner_id"],
        }

    @classmethod
    def format_from_get(cls, product) -> dict:
        return {
            "id": str(product["_id"]),
            "title": product["title"],
            "description": product["description"],
            "price": product["price"],
            "category": product["category"],
            "owner_id": product["owner_id"],
        }
