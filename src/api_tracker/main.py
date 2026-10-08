from fastapi import FastAPI

from api_tracker.feature.task.router import router as task_router

app = FastAPI(title="API Task Tracker")
app.include_router(task_router)
