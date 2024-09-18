from sqlalchemy.orm import Session
from .database import engine, Base, SessionLocal
from src.models import User, Group, Itinerary, GroupMember, ItineraryEvent
import json
import pymysql
import os
from dotenv import load_dotenv

ENV = os.getenv("FASTAPI_ENV", "development")

if ENV == "development":
    load_dotenv(".env.development")
# the production URL is given and loaded directly by railway

# Function to create the database if it doesn't exist

def create_database():
    connection = pymysql.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        port=int(os.getenv('DB_PORT')),
    )
    with connection.cursor() as cursor:
        name=os.getenv('DB_NAME')
        cursor.execute(f"DROP DATABASE IF EXISTS {name};")
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {name};")
    connection.close()


# Seed the database with initial data
def seed_data(db: Session):
    # Load data from JSON files
    with open('src/db/data/users.json') as file:
        users = json.load(file)

    with open('src/db/data/groups.json') as file:
        groups = json.load(file)

    with open('src/db/data/group_members.json') as file:
        group_members = json.load(file)

    with open('src/db/data/itineraries.json') as file:
        itineraries = json.load(file)

    with open('src/db/data/itinerary_events.json') as file:
        itinerary_events = json.load(file)

    # Add data to the session
    for user in users:
        db.add(User(**user))
    db.commit()

    for group in groups:
        db.add(Group(**group))
    db.commit()

    for group_member in group_members:
        db.add(GroupMember(**group_member))
    db.commit()

    for itinerary in itineraries:
        db.add(Itinerary(**itinerary))
    db.commit()

    for itinerary_event in itinerary_events:
        db.add(ItineraryEvent(**itinerary_event))
    db.commit()


# If this script is run directly, seed the database
if __name__ == "__main__":
    # Step 1: Create the database
    if ENV == "development":
        create_database()
    else:
        Base.metadata.drop_all(bind=engine)

    # Step 2: Setup the database tables before seeding
    Base.metadata.create_all(bind=engine)


    db = SessionLocal()
    try:
        seed_data(db)
        print("Database seeded successfully.")
    finally:
        db.close()