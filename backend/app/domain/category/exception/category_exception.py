from fastapi import HTTPException


class CategoryNotFoundException(HTTPException):
    def __init__(self, category_id: int):
        super().__init__(
            status_code=404, detail=f"Category with ID {category_id} not found"
        )
