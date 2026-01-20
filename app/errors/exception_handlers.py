from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.errors.errors import AlreadyExistsError, NotFoundError


def setup_error_handlers(app: FastAPI) -> None:
    """Объявляет обработчики ошибок приложения.

    Args:
        app (FastAPI): Приложение FastAPI.

    Returns:
        None: None.
    """

    @app.exception_handler(NotFoundError)
    async def entity_not_found_error_handler(
        request: Request,  # noqa
        exc: NotFoundError,
    ) -> JSONResponse:
        """Обработчик ошибки отсутствия искомой сущности в базе данных.
        Возвращает JSON ответ с информацией об ошибке.

        Args:
            request (Request): Информация о совершенном запросе.
            exc (NotFoundError): Исключение перехваченное обработчиком.

        Returns:
            JSONResponse: JSON ответ.
        """

        return JSONResponse(
            content=exc.message,
            status_code=exc.status
        )

    @app.exception_handler(AlreadyExistsError)
    async def entity_already_exists_error_handler(
        request: Request,  # noqa
        exc: AlreadyExistsError,
    ) -> JSONResponse:
        """Обработчик ошибки существования создаваемой сущности в базе данных.
        Возвращает JSON ответ с информацией об ошибке.

        Args:
            request (Request): Информация о совершенном запросе.
            exc (NotFoundError): Исключение перехваченное обработчиком.

        Returns:
            JSONResponse: JSON ответ.
        """
        return JSONResponse(
            content=exc.message,
            status_code=exc.status
        )

    @app.exception_handler(RequestValidationError)
    async def pydantic_validation_error_handler(
        request: Request,  # noqa
        exc: RequestValidationError
    ) -> JSONResponse:
        """Обработчик ошибки валидации поля pydantic схемы. Возвращает JSON
        ответ с информацией об ошибке.

        Args:
            request (Request): Информация о совершенном запросе.
            exc (NotFoundError): Исключение перехваченное обработчиком.

        Returns:
            JSONResponse: JSON ответ.
        """
        errors_description = []
        errors = exc.errors()
        for error in errors:
            errors_description.append(
                f'При валидации поля {error.get('loc')[-1]} '
                f'возникла ошибка: {error.get('msg')}'
                )
        return JSONResponse(
            content=errors_description,
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT
        )
