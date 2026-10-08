from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api_tracker.feature.task.router import router as task_router

app = FastAPI(title="API Task Tracker")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(task_router)
