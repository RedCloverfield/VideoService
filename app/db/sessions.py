from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.config import get_db_url

engine = create_async_engine(get_db_url())
session_factory = async_sessionmaker(bind=engine, expire_on_commit=False)
