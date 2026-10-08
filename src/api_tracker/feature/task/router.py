from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from api_tracker.core.database import get_db
from api_tracker.feature.task.models import Task
from api_tracker.feature.task.schemas import TaskCreate, TaskRead, TaskUpdate

router = APIRouter(prefix="/task", tags=["task"])


def _get_or_404(db: Session, task_id: int) -> Task:
    task = db.get(Task, task_id)
    if task is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Task not found")
    return task


@router.get("", response_model=list[TaskRead])
def list_tasks(db: Session = Depends(get_db)):
    return db.scalars(select(Task).order_by(Task.id)).all()


@router.post("", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
def create_task(body: TaskCreate, db: Session = Depends(get_db)):
    task = Task(**body.model_dump())
    db.add(task)
    db.commit()
    return task


@router.get("/{task_id}", response_model=TaskRead)
def get_task(task_id: int, db: Session = Depends(get_db)):
    return _get_or_404(db, task_id)


@router.put("/{task_id}", response_model=TaskRead)
def update_task(task_id: int, body: TaskUpdate, db: Session = Depends(get_db)):
    task = _get_or_404(db, task_id)
    for key, value in body.model_dump().items():
        setattr(task, key, value)
    db.commit()
    return task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db.delete(_get_or_404(db, task_id))
    db.commit()
