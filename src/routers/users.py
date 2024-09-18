from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.schemas import UserCreate, UserLogin, UserResponse, GroupResponse
from src.models import User, GroupMember
from src.db.database import get_db
import bcrypt
from typing import List


def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

router = APIRouter()

@router.post('/user', response_model=UserResponse)
def get_user(user: UserLogin, db: Session = Depends(get_db)) -> UserResponse:
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user is None or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=404, detail="Invalid email or password")
    return db_user

@router.post('/', response_model=UserResponse)
def post_user(user: UserCreate, db: Session = Depends(get_db)) -> UserResponse:
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already in use")

    new_user = User(
        email=user.email,
        username=user.username,
        password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)  

    return new_user


# gets all the groups for a given user
@router.get('/{user_id}/groups', response_model=List[GroupResponse])
def get_user_groups(user_id: int, db: Session = Depends(get_db)):
    group_memberships = db.query(GroupMember).filter(GroupMember.user_id == user_id).all()
    
    if not group_memberships:
        raise HTTPException(status_code=404, detail="User not found or no groups found")

    # Extract groups from memberships
    groups = [membership.group for membership in group_memberships]

    return groups