from fastapi import HTTPException, status

# exceptions.py
class CustomException(Exception):
    pass

class TestException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="test",
        )