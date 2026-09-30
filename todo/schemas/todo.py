from datetime import datetime

from pydantic import BaseModel, PositiveInt, ValidationError, PositiveFloat, ConfigDict
from typing import Annotated, Literal, List
from annotated_types import Gt, Ge, Le
from pydantic import Field, StringConstraints

# 화면단하고 서버단하고 데이터 주고 받을 때 사용
# API 요청/응답 데이터 구조
# todo 1개


class TodoCreate(BaseModel):
    """
    Todo 입력 요청
    """

    title: str
    completed: bool | None = None
    important: bool | None = None


class TodoUpdate(BaseModel):
    """
    Todo 수정 요청
    """

    title: str | None = None
    completed: bool | None = None
    important: bool | None = None


class TodoResponse(TodoCreate):
    """
    Todo 응답
    """

    id: int
    created_at: datetime
    updated_at: datetime


class TodoPageResponse(BaseModel):
    items: list[TodoResponse]
    total: int
    total_pages: int
    page: int
    size: int
    completed: bool | None


# class TodoItem(BaseModel):

#     id: int
#     title: str
#     completed: bool
#     important: bool


# class Todo(BaseModel):
#     todos: List[TodoItem]

#     # Swagger/OpenAPI 문서에 보여줄 환경설정
#     model_config = ConfigDict(
#         json_schema_extra={
#             "example": {
#                 "todos": [
#                     {
#                         "id": 0,
#                         "title": "sample title",
#                         "completed": True,
#                         "important": False,
#                     },
#                 ]
#             }
#         }
#     )
