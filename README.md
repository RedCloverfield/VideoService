# Проект для работы с видео VideoService

Проект VideoService — это сервис для создания, хранения и взаимодействия с хранимыми видео.
Ключевые возможности сервиса:

* создание видео;
* получение видео по идентификатору;
* получение списка видео по переданным в запросе параметрам фильтрации;
* обновления статуса видео.

Пользовательский интерфейс сервиса — Swagger документация, позволяющая осуществлять все вышеуказанные операции. 

## Стэк используемых технологий
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![SQLAlchemy](https://img.shields.io/badge/sqlalchemy-%23D71F00.svg?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Pydantic](https://img.shields.io/badge/pydantic-%23E92063.svg?style=for-the-badge&logo=pydantic&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
[Alembic](https://alembic.sqlalchemy.org/)
[Uvicorn](https://uvicorn.dev/)

## Разворачивание проекта в Docker-сети

> [!NOTE]
> Перед началом работы убедитесь, что на машине, на которой производится запуск данного проекта установлен Docker.

1. Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/RedCloverfield/VideoService.git
```

```
cd VideoService
```
2. Создать файл .env со структурой подобной структуре файла .env.example

```
POSTGRES_HOST=db
POSTGRES_DB=your-database-name
POSTGRES_USER=your-database-user
POSTGRES_PASSWORD=your-database-password
```
3. Запустить контейнеризацию приложения через docker compose

```
sudo docker compose up --build
````

Если все шаги проделаны правильно, приложение станет доступно по URL: http://localhost:8000/api/v1/docs.
Для остановки приложение и всех Docker контейнеров воспользуйтесь терминальной компандой

```
sudo docker compose down
````

## Автор проекта
[Ефимов Станислав](https://github.com/RedCloverfield)