from pydantic import BaseModel


class ProductResponse(BaseModel):
    id: str
    title: str
    description: str
    price: float
    category_id: str
    owner_id: str
