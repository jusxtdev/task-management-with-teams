from pydantic import BaseModel

from datetime import datetime

class TeamCreate(BaseModel):
    name : str

class TeamResponse(BaseModel):
    id : int
    name : str
    create_at : datetime
    update_at : datetime