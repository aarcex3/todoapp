"""
App dependecies
"""

import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """App settings"""

    DB_URL: str = str(os.getenv("DB_URL", "database.sqlite3"))


SETTINGS = Settings()
