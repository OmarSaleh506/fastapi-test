import sqlalchemy as sa

class User(Base, Defaults):
    email = sa.Column(sa.String, nullable=False, unique=True)
    password= sa.Column(sa.String, nullable=True)
        
    