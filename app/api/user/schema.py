from pydantic import BaseModel, EmailStr

class CreateUser(BaseModel):
    email:EmailStr
    password:str

class UserResponse(BaseModel):
        email:str
        password:str