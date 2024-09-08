from typing import Optional

from beanie import Document, PydanticObjectId
from pydantic import Field


class ProductDocument(Document):
    id: Optional[PydanticObjectId] = Field(None, alias="_id")
    title: str
    description: str
    price: float
    category_id: PydanticObjectId
    owner_id: str

    class Settings:
        collection = "products"

    def dict(self, *args, **kwargs):
        product_dict = super().dict(*args, **kwargs)
        if "_id" in product_dict:
            product_dict["id"] = str(product_dict.pop("_id"))
        return product_dict
