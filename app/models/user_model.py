from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    email: str
from sqlalchemy import Column, Integer, String
from app.db.base import Base  # SQLAlchemy Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, nullable=True)

