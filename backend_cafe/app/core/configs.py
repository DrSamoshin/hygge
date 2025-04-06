import logging
import os

from pydantic import BaseModel
from pydantic_settings import BaseSettings


class Run(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000

class Logging(BaseModel):
    logging.basicConfig(
        level= logging.INFO,
        format="%(levelname)-9s %(asctime)s - %(module)-15s - %(message)s",
    )

class DataBase(BaseModel):
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_PORT: str = os.getenv("DB_PORT", "5432")
    DB_USER: str = os.getenv("DB_USER", "myuser")
    DB_PASS: str = os.getenv("DB_PASSWORD", "mypassword")
    DB_NAME: str = os.getenv("DB_NAME", "mydb")
    DATABASE_URL: str = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


class Settings(BaseSettings):
    run: Run = Run()
    logging: Logging = Logging()
    data_base: DataBase = DataBase()

settings = Settings()