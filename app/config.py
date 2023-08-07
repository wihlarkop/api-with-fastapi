from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


@lru_cache
class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    DEBUG: bool


settings = Settings()
