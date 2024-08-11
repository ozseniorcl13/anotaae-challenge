import uuid
from typing import Optional

from pydantic import BaseModel


class Product(BaseModel):
    id: Optional[str] = None
    title: str
    description: str
    price: float
    category_id: str
    owner_id: str

    def __init__(self, **data):
        super().__init__(**data)
        if self.id is None:
            self.id = str(uuid.uuid4())
