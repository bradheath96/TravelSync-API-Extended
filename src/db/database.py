from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os


ENV = os.getenv("FASTAPI_ENV", "development")

if ENV == "development":
    load_dotenv(".env.development")
# the production URL is given and loaded directly by railway

DATABASE_URL = os.getenv("MYSQL_URL")

print(DATABASE_URL)


engine = create_engine(DATABASE_URL) # Establishes a connection to the database (database must already exist for this)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # we use session to set these engine configurations and can use sessionlocal without having to repeat this config
# autocommit means changes to db arent automatically comitted, we have to commit the changes (safer that way)
# bind just binds the engine with the session (config) that we specified

Base = declarative_base() 
# creates a base class for all the SQLAlchemy models to inherit 
# By inheriting from Base, the model classes are automatically linked to SQLAlchemy, and they can be mapped to tables in the db



def get_db():
    db = SessionLocal()
    # this function generates a new instance of the session (db)
    # we create an instance of session each time we do a db request then close after
    try:
        yield db
    finally:
        db.close()

