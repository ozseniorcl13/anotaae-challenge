from fastapi import HTTPException, status


class ProductNotFoundException(HTTPException):
    def __init__(self, category_id: int):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with ID {category_id} not found",
        )


class InvalidIdException(HTTPException):
    def __init__(self, invalid_id: int):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"The id {invalid_id} is invalid",
        )
