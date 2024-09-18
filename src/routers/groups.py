from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.schemas import GroupCreate, GroupResponse, GroupMemberResponse, ItineraryResponse
from src.models import Group, Itinerary
from src.db.database import get_db
from .utils import generate_join_code

router = APIRouter()



# gets a group from group_id
@router.get('/{group_id}', response_model=GroupResponse)
def get_group_by_id(group_id: int, db: Session = Depends(get_db)) -> GroupResponse:
    db_group = db.query(Group).filter(Group.id == group_id).first()
    return db_group


# Adds a new group
@router.post('/', response_model=GroupResponse)
def post_group(group: GroupCreate, db: Session = Depends(get_db)) -> GroupMemberResponse:

    join_code = generate_join_code()

    # Check for unique join code in database
    while db.query(Group).filter(Group.join_code == join_code).first() is not None:
        join_code = generate_join_code()  
    
    new_group = Group(
        name=group.name,
        join_code=join_code
    )

    db.add(new_group)
    db.commit()
    db.refresh(new_group)  

    return new_group

# deletes a group
@router.delete('/{group_id}', response_model=GroupResponse)
def delete_group(group_id: int, db: Session = Depends(get_db)) -> GroupResponse:
    db_group = db.query(Group).filter(Group.id == group_id).first()
    if db_group is None:
        raise HTTPException(status_code=404, detail='Group not found')
    db.delete(db_group)
    db.commit()
    return db_group


# update the group order
@router.patch('/{group_id}', response_model=GroupResponse)
def update_group(group_id: int, group: GroupCreate, db: Session = Depends(get_db)) -> GroupMemberResponse:
    db_group = db.query(Group).filter(Group.id == group_id).first()

    if not db_group:
        raise HTTPException(status_code=404, detail="Group not found")

    group_data = group.model_dump(exclude_unset=True)
    for key, value in group_data.items():
        setattr(db_group, key, value)
    
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    
    return db_group


@router.get('/{group_id}/itinerary', response_model=ItineraryResponse)
def get_itinerary_by_group_id(group_id: int, db: Session = Depends(get_db)) -> ItineraryResponse:
    db_itinerary = db.query(Itinerary).filter(Itinerary.group_id == group_id).first()
    return db_itinerary