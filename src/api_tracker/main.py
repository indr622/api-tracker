from contextlib import asynccontextmanager

from fastapi import FastAPI

from api_tracker.core.database import Base, engine
from api_tracker.feature.task.router import router as task_router


@asynccontextmanager
async def lifespan(_: FastAPI):
    Base.metadata.create_all(engine)
    yield


app = FastAPI(title="API Task Tracker", lifespan=lifespan)
app.include_router(task_router)
