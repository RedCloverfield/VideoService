from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import registry

from app.config import get_db_url

metadata = MetaData()
mapper_registry = registry()
engine = create_async_engine(get_db_url())
session_factory = async_sessionmaker(bind=engine, expire_on_commit=False)
