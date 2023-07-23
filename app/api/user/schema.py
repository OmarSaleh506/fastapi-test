from pydantic import BaseModel, EmailStr

# schema.py
class UserInput(BaseModel):
    name: str

class UserOutput(BaseModel):
    id: int
    name: str



class CreateUser(BaseModel):
    email:EmailStr
    password:str

class UserResponse(BaseModel):
        email:str
        password:str