from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
from typing import List


class settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    app_name: str
    app_version: str
    FILE_ALLOWED_TYPES: List[str]
    FILE_MAX_SIZE: int


@lru_cache()
def get_settings():
    return settings()