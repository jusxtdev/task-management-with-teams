from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from datetime import datetime

from app.base import Base

class User(Base):
    __tablename__ = "users"

    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    username : Mapped[str] = mapped_column(String, unique=True, nullable=False)
    passw_hash : Mapped[str] = mapped_column(String, nullable=False)

    created_at : Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    update_at : Mapped[datetime] = mapped_column(DateTime, onupdate=datetime.now(), default=datetime.now())