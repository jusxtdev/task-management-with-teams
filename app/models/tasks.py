from sqlalchemy import Integer, String, DateTime, Date
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column

from datetime import datetime, date
from enum import Enum

from app.base import Base

## Enumerations
class TaskStatus(str,Enum):
    TODO = "todo"
    DOING = "doing"
    DONE = "done"

class TaskPriority(str,Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

## Models
class Task(Base):
    __tablename__ = "tasks"

    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    title : Mapped[str]= mapped_column(String, nullable=False)
    description : Mapped[str]= mapped_column(String, nullable=True)
    status : Mapped[TaskStatus] = mapped_column(SQLEnum(TaskStatus), nullable=False)
    priority : Mapped[TaskPriority]= mapped_column(SQLEnum(TaskPriority), nullable=False)
    due_date : Mapped[date] = mapped_column(Date, nullable=True)

    created_at : Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    update_at : Mapped[datetime] = mapped_column(DateTime, onupdate=datetime.now(), default=datetime.now())