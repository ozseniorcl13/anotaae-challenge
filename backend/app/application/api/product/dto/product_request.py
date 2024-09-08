from typing import Optional

from pydantic import BaseModel


class ProductCreateDTO(BaseModel):
    title: str
    description: Optional[str]
    price: float
    category_id: str
    owner_id: str


class ProductUpdateDTO(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    category_id: Optional[str] = None
    owner_id: Optional[str] = None
