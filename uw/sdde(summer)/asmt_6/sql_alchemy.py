# Database Initialization

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from file_system_package.models import Base

DATABASE_URL = 'sqlite:///filesystem.db'  # Adjust the database URL as needed
engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)

def create_tables():
    Base.metadata.create_all(engine)

def get_session():
    return Session()
