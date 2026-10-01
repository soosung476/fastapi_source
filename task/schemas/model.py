from datetime import datetime

from pydantic import BaseModel, PositiveInt, ValidationError, PositiveFloat, ConfigDict
from typing import Annotated, Literal, List
from annotated_types import Gt, Ge, Le
from pydantic import Field, StringConstraints


class TaskCreate(BaseModel):
    text: str
    done: bool


class TaskUpdate(BaseModel):
    text: str | None = None
    done: bool | None = None


class TaskResponse(TaskCreate):
    id: int


class TaskPageResponse(BaseModel):
    items: list[TaskResponse]
    total: int
    total_pages: int
    page: int
    size: int
