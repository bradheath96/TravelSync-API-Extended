from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional


class ItineraryBase(BaseModel):
    title: str
    group_id: int
    itinerary_order: Optional[List[int]] = None

class ItineraryCreate(ItineraryBase):
    pass

class ItineraryUpdate(BaseModel):
    itinerary_order: List[int]

class ItineraryResponse(ItineraryBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
