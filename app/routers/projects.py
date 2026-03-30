from typing import List

from fastapi import APIRouter, Depends, HTTPException

from app.routers.auth import get_current_user
from app.schemas import ProjectCreate, ProjectRead, ProjectUpdate
from app.models import Project, User
from app.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()



@router.post("/projects/", response_model=ProjectRead)
def create_project(payload: ProjectCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):

    new_project = Project(
        owner_id=current_user.id,
        name=payload.name,
        description=payload.description)

    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    return new_project

@router.get("/projects/", response_model=List[ProjectRead])
def list_projects(db: Session = Depends(get_db)):
    projects = db.query(Project).all()
    return projects

@router.get("/projects/{project_id}", response_model=ProjectRead)
def project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    return project

@router.patch("/projects/{project_id}", response_model=ProjectRead)
def update_project(project_id: int, payload: ProjectUpdate, db: Session = Depends(get_db)):
    updated_project = db.query(Project).filter(Project.id == project_id).first()
    if not updated_project:
        raise HTTPException(status_code=404, detail="Project not found")
    updated_project.name = payload.name
    updated_project.description = payload.description
    db.commit()
    db.refresh(updated_project)
    return updated_project