from app.api.user.model import User
from app.api.user.schema import CreateUser

async def create_user_(
    body:CreateUser,
):
    user =  User(**body)
    return user