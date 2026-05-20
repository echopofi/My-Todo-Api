from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    postgres_user: str = "postgres"
    postgres_password: str = "postgres"
    postgres_db: str = "todo_db"
    postgres_host: str = "db"
    postgres_port: str = "5432"
    database_url: str = "postgresql://postgres:postgres@db:5432/todo_db"
    jwt_secret_key: str = "dev-secret-key-change-in-production"
    jwt_expiration_minutes: int = 60

    class Config:
        env_file = ".env"


settings = Settings()
