from fastapi import status as http_status


class NotFoundError(Exception):
    """Ошибка отсутствия искомой сущности в базе данных."""

    def __init__(
        self,
        message: str,
        status: int = http_status.HTTP_404_NOT_FOUND,
    ):
        self.message = message
        self.status = status


class AlreadyExistsError(Exception):
    """Ошибка существования создаваемой сущности в базе данных."""

    def __init__(
        self,
        message: str,
        status: int = http_status.HTTP_409_CONFLICT,
    ):
        self.message = message
        self.status = status
