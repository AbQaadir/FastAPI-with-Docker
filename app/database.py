from sqlalchemy import create_engine # create a database engine object that represents the core interface to the database.
from sqlalchemy.ext.declarative import declarative_base # ORM (Object-Relational Mapping) models.
from sqlalchemy.orm import sessionmaker # sessionmaker is a factory for making session objects.

from app.config import settings

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()