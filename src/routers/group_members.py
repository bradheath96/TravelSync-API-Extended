from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.schemas import GroupMemberCreate, GroupMemberResponse, UserResponse, JoinGroupRequest
from src.models import GroupMember, Group, User
from src.db.database import get_db
from typing import List


router = APIRouter()

# gets all the members of a group
@router.get('/{group_id}', response_model=List[UserResponse])
def get_users_in_group(group_id: int, db: Session = Depends(get_db)):
    group = db.query(Group).filter(Group.id == group_id).first()
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    return [member.user for member in group.members]  



@router.post('/join', response_model=GroupMemberResponse)
def join_group(request: JoinGroupRequest, db: Session = Depends(get_db)) -> GroupMemberResponse:
    # check group exists with given join code
    group = db.query(Group).filter(Group.join_code == request.join_code).first()
    if not group:
        raise HTTPException(status_code=404, detail="Invalid join code")

    # check user exists in database
    user = db.query(User).filter(User.id == request.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User does not exist")

    # check user isn't already member of group
    existing_member = db.query(GroupMember).filter(
        GroupMember.group_id == group.id,
        GroupMember.user_id == request.user_id
    ).first()

    if existing_member:
        raise HTTPException(status_code=400, detail="User is already a member of the group")

    # add user to the group
    new_group_member = GroupMember(user_id=request.user_id, group_id=group.id)
    db.add(new_group_member)
    db.commit()
    db.refresh(new_group_member)

    return new_group_member


@router.delete('/{group_id}/members/{user_id}', response_model=GroupMemberResponse)
def delete_member_from_group(group_id: int, user_id: int, db: Session = Depends(get_db)) -> GroupMemberResponse:
    db_member = db.query(GroupMember).filter(GroupMember.user_id == user_id, GroupMember.group_id == group_id).first()
    if db_member is None:
        raise HTTPException(status_code=404, detail='Group member not found')
    db.delete(db_member)
    db.commit()
    return db_member