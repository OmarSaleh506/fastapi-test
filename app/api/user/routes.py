from fastapi import APIRouter
from api.user.schema import CreateUser,UserResponse
from api.user.serivces import create_user_

router = APIRouter()
prefix = "/user"
tags = ["users"]


# router.py
from api.user.serivces import do_something
from api.user.schema import UserInput, UserOutput
from api.user.model import User

@router.post("/user", response_model=UserOutput)
def create_user(user_input: UserInput):
    # Your logic to create a user here
    user = User(name=user_input.name)
    return UserOutput(id=user.id, name=user.name)