from sqlalchemy import Boolean, Column, Integer, String, DateTime, func, ForeignKey
from src.db import Base



class ItineraryEvent(Base):
    __tablename__ = 'itinerary_events'

    id = Column(Integer, primary_key=True, index=True)
    itinerary_id = Column(Integer, ForeignKey('itineraries.id', ondelete='CASCADE'), nullable=False)
    name = Column(String(200), nullable=False)
    coords = Column(String(400), nullable=False)
    place_id = Column(String(400), nullable=False)
    created_at = Column(DateTime, default=func.now())

