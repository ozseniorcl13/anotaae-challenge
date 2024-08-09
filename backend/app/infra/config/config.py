import os
from typing import List, Union

from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    PROJECT_NAME: str = "Catalog API"
    PROJECT_VERSION: str = "0.1.0"
    PROJECT_DESCRIPTION: str = "Catalog API - Anotaae Challenge"

    BACKEND_CORS_SETTINGS: List[Union[AnyHttpUrl, str]] = ["*"]
    USE_DEBUG: bool = os.environ.get("USE_DEBUG", default=False)
    HOST: str = os.environ.get("BACKEND_HOST", default="0.0.0.0")
    PORT: int = int(os.environ.get("BACKEND_PORT", default=4000))

    DB_USER: str = os.environ.get("DB_USERNAME")
    DB_PWD: str = os.environ.get("DB_PASSWORD")
    DB_URL: str = os.environ.get("DB_URL")
    DB_NAME: str = os.environ.get("DB_NAME")


config = Config()
