from functools import lru_cache

from app.services.video_service import VideoService


@lru_cache
def get_service() -> VideoService:
    """Возвращает инициализированный сервис для управления видео."""
    return VideoService()
