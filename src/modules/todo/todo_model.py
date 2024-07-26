from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class Todo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    title: str
    description: str
    is_complete: bool = False
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
