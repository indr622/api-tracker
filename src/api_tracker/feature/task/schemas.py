from pydantic import BaseModel, ConfigDict

from api_tracker.feature.task.models import TaskStatus


class TaskCreate(BaseModel):
    name: str
    description: str = ""
    status: TaskStatus = TaskStatus.draft


class TaskUpdate(BaseModel):
    name: str
    description: str = ""
    status: TaskStatus


class TaskRead(TaskCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
