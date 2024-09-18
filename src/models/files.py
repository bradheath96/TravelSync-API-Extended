from sqlalchemy import Boolean, Column, Integer, String, DateTime, func, ForeignKey
from src.db import Base


class File(Base):
    __tablename__ = 'files'

    id = Column(Integer, primary_key=True, index=True)
    file_name = Column(String(200), nullable=False)
    itinerary_id = Column(Integer, ForeignKey('itineraries.id', ondelete='CASCADE'), nullable=False)
    file_path = Column(String(500), nullable=False)

