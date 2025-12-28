from pydantic import BaseModel

from app.models.tasks import TaskStatus, TaskPriority

from datetime import datetime, date

class TaskCreate(BaseModel):
    title : str
    description : str | None = None
    priority : TaskPriority | None = None
    status : TaskStatus = TaskStatus.TODO
    due_date : date | None = None

class TaskResponse(BaseModel):
    id : int
    title : str 
    description :str | None = None
    status : TaskStatus
    priority : TaskPriority | None = None
    due_date : date | None = None
    
    create_at : datetime
    update_at : datetime