from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import models
from app.models.users import User
from app.models.tasks import Task
from app.models.tags import Tag
from app.models.teams import Team
from app.base import Base

DATABASE_URL = 'sqlite:///./database.db'

enigne = create_engine(
    DATABASE_URL,
    connect_args={'check_same_thread' : False}
)

SessionLocal = sessionmaker(bind=enigne, autocommit=False, autoflush=False)

def init_db():
    Base.metadata.create_all(bind=enigne)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()