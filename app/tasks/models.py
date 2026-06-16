from enum import Enum

from pydantic import BaseModel, ConfigDict


class TaskStatus(str, Enum):
    new = "new"
    in_progress = "in_progress"
    done = "done"


class Task(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    description: str | None = None
    status: TaskStatus

