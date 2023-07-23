import sqlalchemy as sa

# model.py
from db.base import Base

class User(Base):
    __tablename__ = "users"
    id = sa.Column(sa.Integer, primary_key=True)
    #email = sa.Column(sa.String, nullable=False, unique=True)
    #password= sa.Column(sa.String, nullable=True)
    name = sa.Column(sa.String)