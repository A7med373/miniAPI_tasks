from pydantic import BaseModel, ConfigDict, Field, field_validator

from app.tasks.models import TaskStatus


class TaskCreate(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        json_schema_extra={
            "examples": [
                {
                    "title": "Buy milk",
                    "description": "2 liters",
                    "status": "new",
                },
            ],
        },
    )

    title: str = Field(
        ...,
        min_length=1,
        description="Required non-empty task title.",
    )
    description: str | None = Field(
        default=None,
        description="Optional task details.",
    )
    status: TaskStatus = Field(description="Task status.")

    @field_validator("title")
    @classmethod
    def title_must_not_be_blank(cls, value: str) -> str:
        title = value.strip()
        if not title:
            raise ValueError("title must not be blank")
        return title

    @field_validator("description")
    @classmethod
    def normalize_description(cls, value: str | None) -> str | None:
        if value is None:
            return None
        description = value.strip()
        return description or None


class TaskRead(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "examples": [
                {
                    "id": 1,
                    "title": "Buy milk",
                    "description": "2 liters",
                    "status": "new",
                },
            ],
        },
    )

    id: int = Field(description="Task identifier.")
    title: str = Field(description="Task title.")
    description: str | None = Field(default=None, description="Task details.")
    status: TaskStatus = Field(description="Task status.")
