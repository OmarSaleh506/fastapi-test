#config.py

import os

from pathlib import Path
env_path = Path('.') / '.env'

class Settings:
    PROJECT_NAME:str = "Fastapi"
    PROJECT_VERSION: str = "1.0.0"

    POSTGRES_USER : str = 'postgres'
    POSTGRES_PASSWORD = 'secret'
    POSTGRES_SERVER : str = 'localhost'
    POSTGRES_PORT : str = 5432 # default postgres port is 5432
    POSTGRES_DB : str = 'datab'
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

settings = Settings()