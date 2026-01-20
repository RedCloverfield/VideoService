from enum import StrEnum


class VideoStatus(StrEnum):
    """Статусы видео."""

    NEW = 'new'
    TRANSCODED = 'transcoded'
    RECOGNIZED = 'recognized'
