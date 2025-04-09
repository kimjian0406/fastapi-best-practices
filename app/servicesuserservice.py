from app.user_model import User
from app.user_schema import UserCreate
from sqlalchemy.orm import Session
from app.core_security import create_access_token

def create_user(db: Session, user_create: UserCreate):
    db_user = User(email=user_create.email, password=user_create.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if user and user.password == password:
        return user
    return None

def login_user(user: User):
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
