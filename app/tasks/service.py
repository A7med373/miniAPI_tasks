from threading import Lock

from app.tasks.models import Task
from app.tasks.schemas import TaskCreate


class TasksService:
    def __init__(self) -> None:
        self._tasks: list[Task] = []
        self._next_id = 1
        self._lock = Lock()

    def create(self, payload: TaskCreate) -> Task:
        with self._lock:
            task = Task(id=self._next_id, **payload.model_dump())
            self._tasks.append(task)
            self._next_id += 1
            return task

    def get_all(self) -> list[Task]:
        with self._lock:
            return self._tasks.copy()

    def get_by_id(self, task_id: int) -> Task | None:
        with self._lock:
            return next((task for task in self._tasks if task.id == task_id), None)

    def reset(self) -> None:
        with self._lock:
            self._tasks.clear()
            self._next_id = 1


tasks_service = TasksService()
