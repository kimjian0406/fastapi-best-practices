# app/services_user_service.py

from sqlalchemy.orm import Session
from app.models_user import User
from app.schemas_user import UserCreate
from app.utils import get_password_hash

def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

