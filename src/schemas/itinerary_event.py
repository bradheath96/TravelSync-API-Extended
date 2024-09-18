from pydantic import BaseModel
from datetime import datetime

class ItineraryEventBase(BaseModel):
    name: str
    coords: str
    place_id: str
    
class ItineraryEventCreate(ItineraryEventBase):
    pass

class ItineraryEventResponse(ItineraryEventBase):
    itinerary_id: int
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
