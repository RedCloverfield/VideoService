from datetime import datetime
from typing import Optional

from fastapi import Query
from fastapi_filter.contrib.sqlalchemy import Filter
from pydantic import Field

from app.models.models import Video


class VideoFilter(Filter):
    """Фильтр для фильтрации видео по полям."""
    status__in: Optional[list[str]] = Field(
        Query(
            None,
            alias='status',
            description='Фильтрация видео по статусу'
        )
    )
    camera_number__in: Optional[list[int]] = Field(
        Query(
            None,
            alias='camera_number',
            description='Фильтрация видео по номеру камеры'
        )
    )
    location__in: Optional[list[str]] = Field(
        Query(
            None,
            alias='location',
            description='Фильтрация видео по локации')
    )
    start_time__gt: Optional[datetime] = Field(
        Query(
            None,
            alias='start_time_from',
            description='Фильтрация видео по началу записи (начиная с)'
        )
    )
    start_time__lt: Optional[datetime] = Field(
        Query(
            None,
            alias='start_time_to',
            description='Фильтрация видео по началу записи (до)'
        )
    )

    class Constants(Filter.Constants):
        model = Video

    class Config:
        validate_by_name = True
