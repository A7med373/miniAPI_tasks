from fastapi import APIRouter, HTTPException, status

from app.tasks.models import Task
from app.tasks.schemas import TaskCreate, TaskRead
from app.tasks.service import tasks_service

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post(
    "",
    response_model=TaskRead,
    status_code=status.HTTP_201_CREATED,
    summary="Create a task",
    description="Creates a task in memory and returns it with a generated id.",
)
def create_task(payload: TaskCreate) -> Task:
    return tasks_service.create(payload)


@router.get(
    "",
    response_model=list[TaskRead],
    summary="List tasks",
    description="Returns all tasks stored in memory.",
)
def get_tasks() -> list[Task]:
    return tasks_service.get_all()


@router.get(
    "/{task_id}",
    response_model=TaskRead,
    summary="Get a task",
    description="Returns a task by id or 404 when it does not exist.",
    responses={status.HTTP_404_NOT_FOUND: {"description": "Task not found"}},
)
def get_task(task_id: int) -> Task:
    task = tasks_service.get_by_id(task_id)
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )
    return task
