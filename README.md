# Mini Tasks API

Небольшой REST API на FastAPI для управления задачами. Проект показывает базовую структуру FastAPI-сервиса: роутеры, схемы, сервисный слой, валидацию и тесты.

## Возможности

- Создание задачи.
- Получение списка задач.
- Получение задачи по `id`.
- Валидация входных данных через Pydantic.
- Статусы задач: `new`, `in_progress`, `done`.
- Тесты для основных сценариев API.

## Стек

- Python 3.10+
- FastAPI
- Pydantic
- Uvicorn
- Pytest

## Запуск

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

API будет доступен по адресу:

```text
http://127.0.0.1:8000
```

Swagger-документация:

```text
http://127.0.0.1:8000/docs
```

## Тесты

```bash
pytest
```

## Примеры запросов

Создать задачу:

```bash
curl -X POST http://127.0.0.1:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Купить молоко","description":"2 литра","status":"new"}'
```

Получить список задач:

```bash
curl http://127.0.0.1:8000/tasks
```

Получить задачу по `id`:

```bash
curl http://127.0.0.1:8000/tasks/1
```

## Структура

```text
app/main.py            - точка входа FastAPI
app/tasks/router.py    - HTTP-эндпоинты
app/tasks/schemas.py   - Pydantic-схемы
app/tasks/service.py   - бизнес-логика
tests/test_tasks.py    - тесты API
```
