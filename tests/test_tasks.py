import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.tasks.service import tasks_service


@pytest.fixture(autouse=True)
def clean_tasks() -> None:
    tasks_service.reset()


client = TestClient(app)


def test_get_tasks_returns_empty_list() -> None:
    response = client.get("/tasks")

    assert response.status_code == 200
    assert response.json() == []


def test_create_task() -> None:
    response = client.post(
        "/tasks",
        json={
            "title": "Купить молоко",
            "description": "2 литра",
            "status": "new",
        },
    )

    assert response.status_code == 201
    assert response.json() == {
        "id": 1,
        "title": "Купить молоко",
        "description": "2 литра",
        "status": "new",
    }


def test_create_task_trims_text_fields() -> None:
    response = client.post(
        "/tasks",
        json={
            "title": "  Купить молоко  ",
            "description": "   ",
            "status": "new",
        },
    )

    assert response.status_code == 201
    assert response.json() == {
        "id": 1,
        "title": "Купить молоко",
        "description": None,
        "status": "new",
    }


def test_task_ids_are_incremented() -> None:
    first_response = client.post(
        "/tasks",
        json={"title": "Купить молоко", "status": "new"},
    )
    second_response = client.post(
        "/tasks",
        json={"title": "Сделать зарядку", "status": "done"},
    )

    assert first_response.status_code == 201
    assert second_response.status_code == 201
    assert first_response.json()["id"] == 1
    assert second_response.json()["id"] == 2


def test_get_tasks() -> None:
    client.post(
        "/tasks",
        json={"title": "Купить молоко", "description": "2 литра", "status": "new"},
    )
    client.post(
        "/tasks",
        json={"title": "Сделать зарядку", "status": "done"},
    )

    response = client.get("/tasks")

    assert response.status_code == 200
    assert response.json() == [
        {
            "id": 1,
            "title": "Купить молоко",
            "description": "2 литра",
            "status": "new",
        },
        {
            "id": 2,
            "title": "Сделать зарядку",
            "description": None,
            "status": "done",
        },
    ]


def test_get_task_by_id() -> None:
    client.post(
        "/tasks",
        json={"title": "Купить молоко", "description": "2 литра", "status": "new"},
    )

    response = client.get("/tasks/1")

    assert response.status_code == 200
    assert response.json()["title"] == "Купить молоко"


def test_get_task_by_unknown_id_returns_404() -> None:
    response = client.get("/tasks/999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Task not found"}


def test_title_is_required() -> None:
    response = client.post("/tasks", json={"status": "new"})

    assert response.status_code == 422


def test_title_must_not_be_blank() -> None:
    response = client.post("/tasks", json={"title": "   ", "status": "new"})

    assert response.status_code == 422


def test_status_must_be_valid() -> None:
    response = client.post(
        "/tasks",
        json={"title": "Купить молоко", "status": "blocked"},
    )

    assert response.status_code == 422


def test_extra_fields_are_rejected() -> None:
    response = client.post(
        "/tasks",
        json={"title": "Купить молоко", "status": "new", "priority": "high"},
    )

    assert response.status_code == 422
