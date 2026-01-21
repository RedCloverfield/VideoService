from fastapi import APIRouter, status as http_status
from fastapi.responses import Response, RedirectResponse

from app.config import settings

base_router = APIRouter()


@base_router.get(
    '/',
    summary=(
        'Ресурс для редиректа на Swagger документацию при переходе на '
        'эндпоинт api/v1/'
    ),
    include_in_schema=False
)
def index() -> RedirectResponse:
    """Ресурс для редиректа на Swagger документацию при переходе на эндпоинт
    'api/v1/'.
    """
    swagger_url = f'{settings.api_url}/docs'
    return RedirectResponse(url=swagger_url)


@base_router.get(
    '/healthcheck',
    summary='Проверка состояния работоспособности сервиса',
    include_in_schema=False
)
def healthcheck() -> Response:
    """Ресурс для проверки состоянии сервиса."""
    return Response(
        status_code=http_status.HTTP_200_OK
    )
