from datetime import datetime

from pydantic import BaseModel


class Todo(BaseModel):
    """Todo base model from which all other schemas derive"""

    id: int
    title: str
    description: str
    is_complete: bool
    created_at: datetime
    update_at: datetime


class TodoOut(BaseModel):
    """Todo schema for the responses"""

    id: int
    title: str
    description: str
    is_complete: bool


class TodoIn(BaseModel):
    """Todo schema in the DB"""

    title: str
    description: str


class TodoUpdate(BaseModel):
    """Todo update schema"""

    title: str
    description: str
    is_complete: bool
