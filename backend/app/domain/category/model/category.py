from bson import ObjectId
from pydantic import BaseModel


class Category(BaseModel):
    title: str
    description: str
    owner_id: str

    @classmethod
    def format_from_create(cls, category: dict, id: ObjectId) -> dict:
        return {
            "id": str(id),
            "title": category["title"],
            "description": category["description"],
            "owner_id": category["owner_id"],
        }

    @classmethod
    def format_from_get(cls, category) -> dict:
        return {
            "id": str(category["_id"]),
            "title": category["title"],
            "description": category["description"],
            "owner_id": category["owner_id"],
        }
