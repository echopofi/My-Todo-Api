from sqlalchemy.orm import Session
from sqlalchemy import func
import bcrypt

from app.models.user import User
from app.schemas.user import UserRegisterRequest
from app.core.auth import create_access_token


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def verify_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode("utf-8"), hashed.encode("utf-8"))


def register_user(db: Session, request: UserRegisterRequest) -> User:
    existing = db.query(User).filter(
        func.lower(User.email) == request.email.lower()
    ).first()
    if existing:
        return None

    user = User(
        first_name=request.first_name,
        last_name=request.last_name,
        email=request.email,
        password=hash_password(request.password),
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def authenticate_user(db: Session, email: str, password: str) -> dict:
    user = db.query(User).filter(
        func.lower(User.email) == email.lower()
    ).first()
    if not user or not verify_password(password, user.password):
        return None
    token = create_access_token(str(user.id))
    return {"access_token": token, "token_type": "bearer"}
