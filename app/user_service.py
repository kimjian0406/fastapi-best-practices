# app/services/user_service.py
from app.models.user_model import User
from app.schemas.user_schema import UserCreate

# 메모리상 저장소
fake_users_db = []

def create_user(user: UserCreate) -> User:
    new_user = User(
        id=len(fake_users_db) + 1,
        username=user.username,
        email=user.email
    )
    fake_users_db.append(new_user)
    return new_user

