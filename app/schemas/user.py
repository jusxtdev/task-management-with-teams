from pydantic import BaseModel

from datetime import datetime

class UserCreate(BaseModel):
    username : str
    password : str

class UserResponse(BaseModel):
    id :int
    username : int
    passw_hash : str 
    created_at : datetime
    update_at : datetime