from dataclasses import dataclass
from datetime import datetime, timedelta

from app.enums.enums import VideoStatus


@dataclass
class Video:
    """Доменная модель видео."""

    video_path: str
    start_time: datetime
    duration: timedelta
    camera_number: int
    location: str
    status: VideoStatus = VideoStatus.NEW
