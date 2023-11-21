import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8'
    )

    DATABASE_URL: str


load_dotenv()
database_url = os.getenv('DATABASE_URL', 'sqlite:///database.db')
settings = Settings(DATABASE_URL=database_url)
