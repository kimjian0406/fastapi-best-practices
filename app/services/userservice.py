from app.models.user_model import User
from app.schemas.user_schema import UserCreate
from sqlalchemy.orm import Session

def create_user(db: Session, user_create: UserCreate):
    user = User(email=user_create.email, password=user_create.password)  # 실제론 비밀번호 해싱이 필요함
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

