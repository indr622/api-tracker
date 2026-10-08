from sqlalchemy import select

from api_tracker.core.celery_app import celery_app
from api_tracker.core.database import SessionLocal
from api_tracker.feature.task.models import Task, TaskStatus


@celery_app.task(name="task.count_by_status")
def count_by_status() -> dict[str, int]:
    """Background job: jumlah task per status."""
    with SessionLocal() as db:
        statuses = db.scalars(select(Task.status)).all()
    return {s.value: statuses.count(s) for s in TaskStatus}
