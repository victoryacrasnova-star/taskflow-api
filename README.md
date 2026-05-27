# TaskFlow API

## What is this?

This is a backend project for managing the development process.  
It allows users to create projects, tasks, and discussions.

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- JWT Authentication
- Pytest
- Docker
- Docker Compose

## Features

- User registration and JWT authentication
- Protected endpoints
- Project CRUD
- Task CRUD
- Task filtering
- Task discussions/comments
- Pytest API tests
- Docker support

## Tests

The project includes pytest tests for the main API flows:

- user registration
- user login
- protected endpoints
- project creation
- task creation

Run tests:

```bash
pytest
```

## Run with Docker

Build and start containers:

```bash
docker compose up --build
```

Open SWAGGER:
```bash
http://localhost:8000/docs
```

# TaskFlow API

## Что это?

Это backend-проект для управления процессом разработки.  
Он позволяет создавать проекты, задачи и обсуждения.

Проект находится в активной разработке.  
Функциональность постепенно расширяется.

## Стек технологий

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- JWT-аутентификация
- Pytest
- Docker
- Docker Compose

## Что умеет?

- Регистрация и авторизация пользователей  
- Создание и обновление проектов  
- Создание, обновление и удаление задач
- Создание, обновление и удаление комментариев  

## Тесты

В проекте есть pytest-тесты для основных сценариев API:

- регистрация пользователя
- логин пользователя
- защищенные endpoints
- создание проекта
- создание задачи

Запуск тестов:

```bash
pytest
```


---

## Запуск:

## Запуск через Docker

Собрать и запустить контейнеры:

```bash
docker compose up --build
```
Открыть SWAGGER:
```bash
http://localhost:8000/docs
```