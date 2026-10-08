from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import URL


class Settings(BaseSettings):
    """App settings, read from environment or the repo-root .env file."""

    model_config = SettingsConfigDict(env_file=("../.env", ".env"), extra="ignore")

    app_name: str = "Sage API"
    environment: str = "development"
    cors_origins: list[str] = ["http://localhost:5173"]

    db_host: str = "localhost"
    db_port: int = 1434
    db_name: str = "sage"
    db_user: str = "sa"
    db_password: str = ""
    odbc_driver: str = "ODBC Driver 18 for SQL Server"

    jwt_secret: str = "change-me"
    jwt_access_minutes: int = 30

    gemini_api_key: str = ""
    gemini_model: str = "gemini-2.5-flash"
    embedding_model: str = "BAAI/bge-small-en-v1.5"

    @property
    def database_url(self) -> URL:
        return URL.create(
            "mssql+pyodbc",
            username=self.db_user,
            password=self.db_password,
            host=self.db_host,
            port=self.db_port,
            database=self.db_name,
            query={"driver": self.odbc_driver, "TrustServerCertificate": "yes"},
        )


@lru_cache
def get_settings() -> Settings:
    return Settings()
