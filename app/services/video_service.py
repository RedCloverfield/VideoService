from typing import Callable

from sqlalchemy.ext.asyncio import AsyncSession

from app.enums.enums import VideoStatus
from app.errors.errors import NotFoundError, AlreadyExistsError
from app.filters.filters import VideoFilter
from app.models.video_model import Video
from app.repositories.video_repository import VideoRepository
from app.schemas.video_schemas import VideoCreateDTO, VideoResponseDTO


class VideoService:
    """Сервис для управления видео."""

    def __init__(
        self,
        session_factory: Callable[[], AsyncSession],
        repository: VideoRepository
    ):
        self._session_factory = session_factory
        self._repository = repository

    @property
    def repository(self):
        return self._repository

    @property
    def session_factory(self):
        return self._session_factory

    async def post_video(
        self, video_data: VideoCreateDTO
    ) -> VideoResponseDTO:
        """Обращается к VideoRepository и для создания видео.
        Возвращает созданное видео и возвращает видео.

        Args:
            video_data (VideoCreateDTO): Данные создаваемого видео

        Raises:
            AlreadyExistsError: Исключение, если видео по указанному пути
                уже существует.

        Returns:
            VideoResponseDTO: Данные созданного видео.
        """
        async with self.session_factory() as session:
            if await self.repository.get_video_by(
                video_path=video_data.video_path,
                session=session
            ):
                raise AlreadyExistsError(
                    'Видео по указанному пути уже существует!'
                )
            video = Video(
                **video_data.model_dump()
            )
            video = await self.repository.post_video(
                video=video, session=session
            )
            return VideoResponseDTO.model_validate(video)

    async def list_videos(
        self, video_filter: VideoFilter
    ) -> list[VideoResponseDTO | None]:
        """Обращается к VideoRepository и возвращает отфильтрованный список
        видео.

        Args:
            video_filter (VideoFilter): Фильтр для фильтрации видео по
                переданным полям.

        Returns:
            list[Optional[VideoResponseDTO]]: Отфильтрованный по переданным полям
                список видео или пустой список, если видео, удовлетворяющие
                условиям поиска, не найдены.
        """
        async with self.session_factory() as session:
            videos = await self.repository.list_videos(
                video_filter=video_filter, session=session
            )
            return [VideoResponseDTO.model_validate(video) for video in videos]

    async def get_video(self, video_id: int) -> VideoResponseDTO:
        """Обращается к VideoRepository и возвращает видео с указанным
        идентификатором.

        Args:
            video_id (int): Идентификатор видео.

        Raises:
            NotFoundError: Исключение, если видео с указанным идентификатором
                не существует.

        Returns:
            VideoResponseDTO: Данные запрошенного видео.
        """
        async with self.session_factory() as session:
            if video := await self.repository.get_video_by(
                id=video_id, session=session
            ):
                return VideoResponseDTO.model_validate(video)
            raise NotFoundError(
                        'Видео с переданным идентификатором не найдено!'
                    )

    async def update_video_status(
        self, video_id: int, status: VideoStatus
    ) -> VideoResponseDTO:
        """Обращается к VideoRepository для обновления статуса видео.
        Возвращает видео с обновленным статусом.

        Args:
            video_id (int): Идентификатор видео.
            status (VideoStatus): Новый статус видео.

        Returns:
             VideoResponseDTO: Данные обновленного видео.
        """
        async with self.session_factory() as session:
            await self.repository.get_video_by(
                id=video_id, session=session
            )
            video = await self.repository.update_video_status(
                video_id=video_id, status=status, session=session
            )
            return VideoResponseDTO.model_validate(video)
