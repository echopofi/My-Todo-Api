from uuid import UUID

from sqlalchemy.orm import Session

from app.models.todo import Todo, TodoStatus
from app.schemas.todo import TodoCreateRequest, TodoUpdateRequest


def create_todo(db: Session, user_id: UUID, request: TodoCreateRequest) -> Todo:
    todo = Todo(
        user_id=user_id,
        title=request.title,
        body=request.body,
    )
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo


def get_user_todos(db: Session, user_id: UUID) -> list[Todo]:
    return db.query(Todo).filter(Todo.user_id == user_id).all()


def get_todo_by_id(db: Session, todo_id: UUID) -> Todo:
    return db.query(Todo).filter(Todo.id == todo_id).first()


def update_todo(db: Session, todo: Todo, request: TodoUpdateRequest) -> Todo:
    update_data = request.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(todo, key, value)
    db.commit()
    db.refresh(todo)
    return todo


def delete_todo(db: Session, todo: Todo) -> None:
    db.delete(todo)
    db.commit()
