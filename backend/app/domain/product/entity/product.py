from typing import Optional

from pydantic import BaseModel


class Product(BaseModel):
    id: Optional[str] = None
    title: str
    description: Optional[str] = None
    price: float
    category_id: str
    owner_id: str

    def update_values(self, update_data: dict):
        for key, value in update_data.items():
            if value is not None:
                setattr(self, key, value)
