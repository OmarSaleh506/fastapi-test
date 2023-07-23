from api.user.model import User
from api.user.schema import CreateUser

# services.py
def do_something():
    # Your service logic here
    pass

async def create_user_(
    body:CreateUser,
):
    user =  User(**body)
    return user
