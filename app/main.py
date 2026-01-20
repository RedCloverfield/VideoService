from fastapi import FastAPI

from app.config import settings
from app.errors.exception_handlers import setup_error_handlers
from app.routers.base_router import base_router
from app.routers.video_router import video_router


def create_and_setup_app() -> FastAPI:
    """Создает и возвращает FastAPI приложение с подключенными обработчиками
    ошибок и роутерами.
    """
    app = FastAPI(
        title=settings.api_title,
        root_path="/api/v1",
    )
    setup_error_handlers(app=app)
    app.include_router(router=video_router)
    app.include_router(router=base_router)
    return app


app = create_and_setup_app()
