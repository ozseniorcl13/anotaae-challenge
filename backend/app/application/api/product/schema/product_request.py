from unicodedata import category
from pydantic import BaseModel


class ProductRequest(BaseModel):
    title: str
    description: str
    price: float
    category: str
    owner_id: str
