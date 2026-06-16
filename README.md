# Mini Tasks API

Небольшой REST API для списка задач на FastAPI.

## Запуск

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

API будет доступен на `http://127.0.0.1:8000`.

Проект рассчитан на Python 3.10+.

## Тесты

```bash
pytest
```

## Эндпоинты

### `POST /tasks`

Создает новую задачу.

```bash
curl -X POST http://127.0.0.1:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Купить молоко","description":"2 литра","status":"new"}'
```

Пример ответа:

```json
{
  "id": 1,
  "title": "Купить молоко",
  "description": "2 литра",
  "status": "new"
}
```

### `GET /tasks`

Возвращает все задачи.

```bash
curl http://127.0.0.1:8000/tasks
```

### `GET /tasks/{task_id}`

Возвращает одну задачу по id.

```bash
curl http://127.0.0.1:8000/tasks/1
```

Если задачи нет, API вернет `404 Not Found`.

## Поля задачи

`title` - обязательная непустая строка.

`description` - необязательная строка.

`status` - одно из значений: `new`, `in_progress`, `done`.
