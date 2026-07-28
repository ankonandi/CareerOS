from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseModel):
    """Database configuration settings.

    Structures and formats individual database credentials.
    """

    user: str
    password: str
    db: str
    host: str
    port: int

    @property
    def url(self) -> str:
        """Returns the PostgreSQL DSN connection URL for SQLAlchemy.

        Uses the recommended 'postgresql+psycopg' driver (Psycopg 3)
        as per SQLAlchemy 2.0 guidelines.
        """
        return f"postgresql+psycopg://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}"


class Settings(BaseSettings):
    """Application-wide configuration settings loaded from environment.

    Loads and parses environment variables. Fields are grouped and structured
    for type-safe consumption throughout the service layers.
    """

    model_config = SettingsConfigDict(
        # Look for environment files in both root and backend contexts
        env_file=(".env", "backend/.env", "../.env"),
        env_file_encoding="utf-8",
        # Ignore external/extra environment variables not in schema
        extra="ignore",
    )

    # General Application Environment Configuration
    env: str = Field(default="development", validation_alias="ENV")

    # PostgreSQL Credentials mapped from standard flat configuration names
    postgres_user: str = Field(default="postgres", validation_alias="POSTGRES_USER")
    postgres_password: str = Field(
        default="postgres_secure_pass_change_me",
        validation_alias="POSTGRES_PASSWORD",
    )
    postgres_db: str = Field(default="careeros", validation_alias="POSTGRES_DB")
    postgres_host: str = Field(default="localhost", validation_alias="POSTGRES_HOST")
    postgres_port: int = Field(default=5432, validation_alias="POSTGRES_PORT")

    @property
    def db(self) -> DatabaseSettings:
        """Returns a structured, typed DatabaseSettings configuration object."""
        return DatabaseSettings(
            user=self.postgres_user,
            password=self.postgres_password,
            db=self.postgres_db,
            host=self.postgres_host,
            port=self.postgres_port,
        )


# Singleton settings instance to import throughout the app
settings = Settings()
