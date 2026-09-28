from datetime import datetime

from pydantic import BaseModel, PositiveInt, ValidationError, PositiveFloat, ConfigDict
from typing import Annotated, Literal, List
from annotated_types import Gt, Ge, Le
from pydantic import Field, StringConstraints


class Task(BaseModel):
    id: int
    text: str
    done: bool
