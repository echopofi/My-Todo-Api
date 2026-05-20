from datetime import datetime
from uuid import UUID
from typing import Optional

from pydantic import BaseModel

from app.models.todo import TodoStatus


class TodoCreateRequest(BaseModel):
    title: str
    body: str


class TodoUpdateRequest(BaseModel):
    title: Optional[str] = None
    body: Optional[str] = None
    status: Optional[TodoStatus] = None


class TodoResponse(BaseModel):
    id: UUID
    title: str
    body: str
    status: TodoStatus
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
