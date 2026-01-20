from datetime import datetime, timedelta

from pydantic import BaseModel, Field, ConfigDict

from app.enums.enums import VideoStatus


class VideoCreateDTO(BaseModel):
    """Схема для создания видео."""

    video_path: str = Field(description='Путь до видеофайла', min_length=1)
    start_time: datetime = Field(description='Время начала записи')
    duration: timedelta = Field(description='Длительность видео', gt=0)
    camera_number: int = Field(description='Номер камеры', gt=0)
    location: str = Field(description='Локация камеры', min_length=1)

    model_config = ConfigDict(ser_json_timedelta='float')


class VideoResponseDTO(VideoCreateDTO):
    """Схема ответа, содержащая данные о видео."""

    id: int = Field(description='Идентификатор видео')
    status: VideoStatus

    model_config = ConfigDict(from_attributes=True)
