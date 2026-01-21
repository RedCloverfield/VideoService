from typing import Annotated

from fastapi import APIRouter, Depends, status as http_status
from fastapi_filter import FilterDepends
from fastapi.responses import Response, JSONResponse

from app.dependencies.dependencies import get_video_service
from app.enums.enums import VideoStatus
from app.filters.filters import VideoFilter
from app.schemas.video_schemas import VideoCreateDTO, VideoResponseDTO
from app.services.video_service import VideoService

video_router = APIRouter(prefix="/videos", tags=['videos'])


@video_router.post(
    '/',
    summary='Создать видео',
    description=(
        'Ресурс для создания видео. Возвращает данные созданного видео'
    )
)
async def post_video(
    video_data: VideoCreateDTO,
    service: Annotated[VideoService, Depends(get_video_service)]
) -> VideoResponseDTO:
    """Ресурс для создания видео. Возвращает данные созданного видео.

    Args:
        video_data (VideoCreateDTO): Данные создаваемого видео.
        service (VideoService): Сервис для управления видео.

    Returns:
        VideoResponseDTO: Данные созданного видео.
    """
    return await service.post_video(video_data=video_data)


@video_router.get(
    '/',
    summary='Получить отфильтрованный список видео',
    description='Ресурс для получения отфильтрованного списка видео'
)
async def list_videos(
    service: Annotated[VideoService, Depends(get_video_service)],
    video_filter: Annotated[VideoFilter, FilterDepends(VideoFilter)]
) -> list[VideoResponseDTO | None]:
    """Ресурс для получения отфильтрованного списка видео.

    Args:
        service (VideoService): Сервис для управления видео.
        video_filter (VideoFilter): Фильтр для фильтрации видео по переданным
            полям.

    Returns:
        list[Optional[VideoResponseDTO]]: Отфильтрованный список видео или
            пустой список, если видео, удовлетворяющие условиям поиска, не были
            найдены.
    """
    return await service.list_videos(video_filter=video_filter)


@video_router.get(
    '/{video_id}',
    summary='Получить видео по идентификатору',
    description='Ресурс для получения видео по идентификатору'
)
async def get_video(
    video_id: int,
    service: Annotated[VideoService, Depends(get_video_service)]
) -> VideoResponseDTO:
    """Ресурс для получения видео по идентификатору.

    Args:
        video_id (int): Идентификатор видео.
        service (VideoService): Сервис для управления видео.

    Returns:
        VideoResponseDTO: Данные запрошенного видео.
    """
    return await service.get_video(video_id=video_id)


@video_router.patch(
    '/{video_id}/status',
    summary='Измененить статус видео',
    description=(
        'Ресурс для изменения статуса видео. Возвращает видео с обновленным '
        'статусом'
    )
)
async def update_video_status(
    video_id: int,
    status: VideoStatus,
    service: Annotated[VideoService, Depends(get_video_service)]
) -> VideoResponseDTO:
    """Ресурс для изменения статуса видео. Возвращает видео с обновленным
    статусом.

    Args:
        video_id (int): Идентификатор видео.
        status (VideoStatus): Новый статус видео.
        service (VideoService): Сервис для управления видео.

    Returns:
        VideoResponseDTO: Данные обновленного видео.
    """
    return await service.update_video_status(
        video_id=video_id, status=status
    )
