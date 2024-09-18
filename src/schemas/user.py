from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserLogin(BaseModel):
    username: str
    password: str

class UserCreate(UserBase):
    password: str  # This is the raw password that will be hashed

class UserResponse(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True  # Allows Pydantic to work with SQLAlchemy models directly
