from sqlalchemy.orm import Session
from app.models.models_user import User
from app.schemas.schemas_user import UserCreate
from app.core.security import get_password_hash


def create_user(db: Session, user: UserCreate):
    hashed_pw = get_password_hash(user.password)
    db_user = User(
        username=user.email.split("@")[0],  # 간단한 예: 이메일 앞부분을 username으로
        email=user.email,
        hashed_password=hashed_pw,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()
