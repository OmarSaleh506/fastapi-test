from fastapi import APIRouter
from app.api.user.schema import CreateUser,UserResponse

from app.api.user.services.create_user import create_user_

router = APIRouter()
prefix = "/user"
tags = ["user"]


@router.post(
    "",
    dependencies=[]
)
async def create_user(
    body=CreateUser,
    
)-> UserResponse:
    return await create_user_(body=body)