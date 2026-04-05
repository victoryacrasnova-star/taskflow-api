
from app.models import Task, Project
from app.schemas import TaskCreate, TaskRead, TaskUpdate
from fastapi import APIRouter, Depends, HTTPException
from app.database import get_db
from sqlalchemy.orm import Session
from typing import List


router = APIRouter()

@router.post("/projects/{project_id}/tasks", response_model=TaskRead)
async def create_task(project_id:int, payload: TaskCreate, db: Session = Depends(get_db)):

    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    new_task = Task(
        assignee_id=payload.assignee_id,
        project_id=project_id,

        description=payload.description,
        title=payload.title
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task

@router.get("/projects/{project_id}/tasks", response_model=List[TaskRead])
async def get_tasks(project_id: int, db: Session = Depends(get_db)):

    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    tasks = db.query(Task).filter(Task.project_id == project_id).all()

    return tasks

@router.get("/projects/{project_id}/tasks/{task_id}", response_model=TaskRead)
async def get_task(project_id: int, task_id: int, db: Session = Depends(get_db)):

    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if task.project_id != project_id:
        raise HTTPException(status_code=404, detail="Task not found in this project")

    return task

@router.patch("/projects/{project_id}/tasks/{task_id}", response_model=TaskRead)
async def update_task(project_id:  int, task_id: int, payload: TaskUpdate, db: Session = Depends(get_db)):
    updated_task = db.query(Task).filter(Task.project_id == project_id).filter(Task.id == task_id).first()
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")

    if payload.title is not None:
        updated_task.title = payload.title

    if payload.description is not None:
        updated_task.description = payload.description

    if payload.status is not None:
        updated_task.status = payload.status

    if payload.assignee_id is not None:
        updated_task.assignee_id = payload.assignee_id

    db.commit()
    db.refresh(updated_task)
    return updated_task

@router.delete("/projects/{project_id}/tasks/{task_id}", response_model=TaskRead)
async def delete_task(project_id: int, task_id: int, db: Session = Depends(get_db)):

    task = db.query(Task).filter(Task.project_id == project_id).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()

    return task