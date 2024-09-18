from sqlalchemy import JSON, Column, Integer, String, DateTime, func, ForeignKey
from src.db import Base


class Itinerary(Base):
    __tablename__ = 'itineraries'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200))
    group_id = Column(Integer, ForeignKey('groups.id', ondelete='CASCADE'), nullable=False)
    itinerary_order = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=func.now())




