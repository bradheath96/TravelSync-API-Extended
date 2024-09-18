from pydantic import BaseModel
from datetime import datetime
from typing import List


class GroupBase(BaseModel):
    name: str

class GroupCreate(GroupBase):
    pass


class GroupResponse(GroupBase):
    id: int
    created_at: datetime
    join_code: str


    class Config:
        orm_mode = True


class JoinGroupRequest(BaseModel):
    user_id: int
    join_code: str