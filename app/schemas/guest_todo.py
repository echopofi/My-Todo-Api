from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class GuestTodoCreateRequest(BaseModel):
    title: str
    body: str


class GuestTodoResponse(BaseModel):
    id: UUID
    title: str
    body: str
    created_at: datetime

    class Config:
        from_attributes = True
