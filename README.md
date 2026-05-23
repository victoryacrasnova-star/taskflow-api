# TaskFlow API

## What is this?

This is a backend project for managing the development process.  
It allows users to create projects, tasks, and discussions.

## Features

- User registration and authentication  
- Create and update projects  
- Create, update and delete tasks  
- Discussions inside tasks
- Create, update and delete comment  

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

## How to run?

1. Clone the repository  
2. Install dependencies  
3. Configure the database connection (using .env)  
4. Run the server:

uvicorn app.main:app --reload

5. Open Swagger:
http://127.0.0.1:8000/docs

# TaskFlow API

## Что это?

Это backend-проект для управления процессом разработки.  
Он позволяет создавать проекты, задачи и обсуждения.

Проект находится в активной разработке.  
Функциональность постепенно расширяется.

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

## Как запустить?

1. Склонировать репозиторий  
2. Установить зависимости  
3. Настроить подключение к базе данных (через .env)  
4. Запустить сервер:

uvicorn app.main:app --reload

5. Открыть Swagger:
http://127.0.0.1:8000/docs
