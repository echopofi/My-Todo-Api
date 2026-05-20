from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.guest_todo import GuestTodoCreateRequest, GuestTodoResponse
from app.services import guest_todo_service

router = APIRouter(prefix="/api/guest/todos", tags=["guest todos"])


@router.post("", response_model=GuestTodoResponse, status_code=status.HTTP_201_CREATED)
def create_guest_todo(
    request: GuestTodoCreateRequest,
    db: Session = Depends(get_db),
):
    return guest_todo_service.create_guest_todo(db, request)


@router.get("", response_model=list[GuestTodoResponse])
def get_guest_todos(
    db: Session = Depends(get_db),
):
    return guest_todo_service.get_all_guest_todos(db)
