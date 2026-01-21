from fastapi import Depends
from typing import Annotated, Callable

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.sessions import get_session_factory
from app.services.video_service import VideoService
from app.repositories.video_repository import VideoRepository


def get_video_repository() -> VideoRepository:
    return VideoRepository()


def get_video_service(
    session_factory: Annotated[
        Callable[[], AsyncSession], Depends(get_session_factory)
        ],
    repository: Annotated[VideoRepository, Depends(get_video_repository)]
) -> VideoService:
    """Возвращает инициализированный сервис для управления видео."""
    return VideoService(
        session_factory=session_factory,
        repository=repository
    )
