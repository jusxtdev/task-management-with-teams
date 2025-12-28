from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from datetime import datetime

from app.base import Base

class Team(Base):
    __tablename__ = "teams"

    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    name : Mapped[str] = mapped_column(String, unique=True, nullable=False)
    
    create_at : Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    update_at : Mapped[datetime] = mapped_column(DateTime, onupdate=datetime.now(), default=datetime.now())
