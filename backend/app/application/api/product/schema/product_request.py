from pydantic import BaseModel


class ProductRequest(BaseModel):
    title: str
    description: str
    price: float
    category_id: str
    owner_id: str
