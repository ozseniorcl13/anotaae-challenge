from typing import Optional

from beanie import Document, PydanticObjectId
from pydantic import Field


class CategoryDocument(Document):
    id: Optional[PydanticObjectId] = Field(None, alias="_id")
    title: str
    description: str
    owner_id: str

    class Settings:
        collection = "categories"

    def dict(self, *args, **kwargs):
        category_dict = super().dict(*args, **kwargs)
        if "_id" in category_dict:
            category_dict["id"] = str(category_dict.pop("_id"))
        return category_dict
