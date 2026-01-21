from sqlalchemy import (
    Column,
    Enum,
    Integer,
    Interval,
    String,
    Table,
    TIMESTAMP,
)

from app.db.registry import metadata
from app.enums.enums import VideoStatus
from app.models.video_model import Video


video_table = Table(
    'video',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('video_path', String, unique=True, nullable=False),
    Column('start_time', TIMESTAMP(timezone=True)),
    Column('duration', Interval),
    Column('camera_number', Integer),
    Column('location', String),
    Column('status', Enum(VideoStatus), default=VideoStatus.NEW)
)
