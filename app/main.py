from typing import Union
from fastapi import FastAPI
from core.config import settings
from db.database import engine 
from db.base import Base
from api.user.routes import router

def create_tables():         
	Base.metadata.create_all(bind=engine)

app = FastAPI()
create_tables()
app.include_router(router)


@app.get("/")
def home():
    return {"msg":"Hello FastAPI🚀"}


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
