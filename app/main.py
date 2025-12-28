from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.database import init_db
#Import routers

@asynccontextmanager
async def lifespan(app : FastAPI):
    # start up 
    await init_db()
    yield

app = FastAPI(lifespan=lifespan)