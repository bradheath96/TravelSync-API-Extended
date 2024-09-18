from sqlalchemy import Boolean, Column, Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship

from src.db import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True)
    email = Column(String(200), unique=True)
    password = Column(String(300), nullable=False)
    created_at = Column(DateTime, default=func.now())

    group_members = relationship("GroupMember", back_populates="user", cascade="all, delete-orphan")


