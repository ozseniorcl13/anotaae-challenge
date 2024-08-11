from unicodedata import category
from pydantic import BaseModel


class ProductResponse(BaseModel):
    id: str
    title: str
    description: str
    price: float
    category: str
    owner_id: str
