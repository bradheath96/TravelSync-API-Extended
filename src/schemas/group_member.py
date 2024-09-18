from pydantic import BaseModel

class GroupMemberBase(BaseModel):
    user_id: int
    group_id: int

class GroupMemberCreate(BaseModel):
    user_id: int

class GroupMemberResponse(GroupMemberBase):
    id: int

    class Config:
        orm_mode = True

