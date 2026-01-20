from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv('.env')


class Settings(BaseSettings):
    api_title: str = 'Проект для работы с видео VideoService'
    api_url: str = 'http://localhost/api/v1'
    postgres_host: str = 'localhost'
    postgres_port: int = 5432
    postgres_db: str
    postgres_user: str
    postgres_password: str

    class Config:
        env_file = '../.env'


settings = Settings()


def get_db_url():
    """Возвращает URL базы данных проекта."""
    return (
        f'postgresql+asyncpg://{settings.postgres_user}:{settings.postgres_password}@'
        f'{settings.postgres_host}:{settings.postgres_port}/{settings.postgres_db}'
    )
