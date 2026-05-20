from sqlalchemy.orm import Session

from app.models.guest_todo import GuestTodo
from app.schemas.guest_todo import GuestTodoCreateRequest


def create_guest_todo(db: Session, request: GuestTodoCreateRequest) -> GuestTodo:
    todo = GuestTodo(
        title=request.title,
        body=request.body,
    )
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo


def get_all_guest_todos(db: Session) -> list[GuestTodo]:
    return db.query(GuestTodo).all()
