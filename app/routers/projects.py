from typing import List

from fastapi import APIRouter, Depends, HTTPException

from app.schemas import ProjectCreate, ProjectRead
from app.models import Project
from app.database import SessionLocal, get_db
from sqlalchemy.orm import Session

router = APIRouter()



@router.post("/projects/", response_model=ProjectRead)
def create_project(payload: ProjectCreate, db: Session = Depends(get_db())):

    new_project = Project(
        owner_id=1, #временно, пока нет get_current_user
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
