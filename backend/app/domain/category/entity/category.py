from typing import Optional

from pydantic import BaseModel


class Category(BaseModel):
    id: Optional[str] = None
    title: str
    description: Optional[str] = None
    owner_id: str

    def update_values(self, update_data: dict):
        for key, value in update_data.items():
            if value is not None:
                setattr(self, key, value)
