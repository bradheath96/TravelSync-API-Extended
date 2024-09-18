from fastapi import FastAPI
from src.routers import users, groups, itineraries, itinerary_events, google_places, group_members
from fastapi.middleware.cors import CORSMiddleware

from src.models import Base  
from src.db import engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

# Allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)


# using tags on routers is just to improve the /docs page accuracy
app.include_router(users.router, prefix="/api/users", tags=["users"])
app.include_router(groups.router, prefix="/api/groups", tags=["groups"])
app.include_router(group_members.router, prefix="/api/group_members", tags=["group_members"])
app.include_router(itineraries.router, prefix="/api/itineraries", tags=["itineraries"])
app.include_router(itinerary_events.router, prefix="/api/itinerary-events", tags=["itinerary events"])
app.include_router(google_places.router, prefix="/api/places", tags=["google places"])


@app.get("/")
async def root():
    return {"message": "Welcome to the TravelSync API"}

