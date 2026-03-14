from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    Name = Column(String)
    Email = Column(String)
    Phone = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    passwordHash = Column(String)
