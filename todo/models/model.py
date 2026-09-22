from datetime import datetime

from pydantic import BaseModel, PositiveInt, ValidationError, PositiveFloat, ConfigDict
from typing import Annotated, Literal, List
from annotated_types import Gt, Ge, Le
from pydantic import Field, StringConstraints

# todo 1개


class TodoItem(BaseModel):
    id: int
    title: str
    completed: bool
    important: bool


class Todo(BaseModel):
    todos: List[TodoItem]

    # Swagger/OpenAPI 문서에 보여줄 환경설정
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "todos": [
                    {
                        "id": 0,
                        "title": "sample title",
                        "completed": True,
                        "important": False,
                    },
                ]
            }
        }
    )
