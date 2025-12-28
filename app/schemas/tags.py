from pydantic import BaseModel

from datetime import datetime

class TagCreate(BaseModel):
    title : str 

class TagResponse(BaseModel):
    id : int
    title : str

    created_at : datetime
    update_at : datetime