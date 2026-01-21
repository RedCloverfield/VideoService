from sqlalchemy import select, update

from app.db.sessions import session_factory
from app.models.video_model import Video
from app.enums.enums import VideoStatus
from app.filters.filters import VideoFilter


class VideoRepository:
    """Репозиторий для осуществленния запросов к базе данных для управления
    видео.
    """

    def __init__(self):
        self.session_factory = session_factory
        self.model = Video

    async def post_video(self, video: Video) -> Video:
        """Создает и возвращает видео.

        Args:
            video (Video): Доменная модель видео.

        Returns:
            Video: Видео.
        """
        async with self.session_factory() as session:
            session.add(video)
            await session.commit()
            return video

    async def list_videos(
        self, video_filter: VideoFilter
    ) -> list[Video | None]:
        """Возвращает отфильтрованный список видео.

        Args:
            video_filter (VideoFilter): Фильтр для фильтрации видео по
                переданным полям.

        Returns:
            list[Optional[Video]]: Отфильтрованный список видео, или пустой
                список, если удовлетворяющих запросу видео нет.
        """
        async with self.session_factory() as session:
            query = video_filter.filter(select(self.model))
            result = await session.execute(query)
            return result.scalars().all()

    async def get_video_by(self, **kwargs) -> Video:
        """Возвращает видео по переданному параметру.

        Returns:
            Video: Видео.
        """
        async with self.session_factory() as session:
            query = select(self.model).filter_by(**kwargs)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    async def update_video_status(
        self, video_id: int, status: VideoStatus
    ) -> Video:
        """Обновляет стаутс видео и возвращает его.

        Args:
            video_id (int): Идентификатор видео.
            status (VideoStatus): Новый статус видео.

        Returns:
            Video: Видео с обновленным статусом.
        """
        async with self.session_factory() as session:
            stmt = (
                update(self.model)
                .filter_by(id=video_id)
                .values(status=status)
                .returning(self.model)
            )
            result = await session.execute(stmt)
            await session.commit()
            return result.scalars().first()
