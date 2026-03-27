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
