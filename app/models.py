from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)

    projects = relationship("Project", back_populates="owner")

    tasks = relationship("Task", back_populates="assignee")

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    owner = relationship("User", back_populates="projects")

    tasks = relationship("Task", back_populates="project")

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String)
    status = Column(String, default="new")

    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    project = relationship("Project", back_populates="tasks")

    assignee_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    assignee = relationship("User", back_populates="tasks")