from app.models import User as UserModel
from app.schemas import User, UserCreate
from sqlalchemy.orm import Session
from typing import List

class UserService:
    
    @staticmethod
    def create_user(user_create: UserCreate, db: Session) -> User:
        db_user = UserModel(name=user_create.name, email=user_create.email)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    def get_users(db: Session) -> List[User]:
        return db.query(UserModel).all()

    @staticmethod
    def get_user(user_id: int, db: Session) -> User:
        db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
        if db_user is None:
            raise ValueError(f"User with ID {user_id} not found")
        return db_user

    @staticmethod
    def update_user(user_id: int, user_update: UserCreate, db: Session) -> User:
        db_user = UserService.get_user(user_id, db)
        db_user.name = user_update.name
        db_user.email = user_update.email
        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    def delete_user(user_id: int, db: Session) -> User:
        db_user = UserService.get_user(user_id, db)
        db.delete(db_user)
        db.commit()
        return db_user

