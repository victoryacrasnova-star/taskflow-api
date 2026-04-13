from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.routers.auth import get_current_user
from app.schemas import CommentRead, CommentCreate, CommentUpdate
from app.models import User, Task, Comment

router = APIRouter()

@router.post("/tasks/{task_id}/comments", response_model=CommentRead)
def create_comment(task_id: int, payload: CommentCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if payload.reply_to_comment_id is not None:
        reply_comment = db.query(Comment).filter(Comment.id == payload.reply_to_comment_id).first()
        if not reply_comment:
            raise HTTPException(status_code=404, detail="Reply comment not found")

        if reply_comment.task_id != task.id:
            raise HTTPException(status_code=400, detail="Reply comment belongs to another task")

    new_comment = Comment(content = payload.content,
                          author_id = current_user.id,
                          reply_to_comment_id = payload.reply_to_comment_id,
                          task_id = task_id)

    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment

@router.get("/tasks/{task_id}/comments", response_model=List[CommentRead])
def read_comments(task_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    comments = db.query(Comment).filter(Comment.task_id == task_id).offset(skip).limit(limit).all()
    return comments

@router.get("/comments/{comment_id}", response_model=CommentRead)
def read_comment(comment_id: int, db: Session = Depends(get_db)):
    comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    return comment

@router.patch("/comments/{comment_id}", response_model=CommentRead)
def update_comment(comment_id: int, payload: CommentUpdate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    if comment.author_id != current_user.id:
        raise HTTPException(status_code=403, detail="You are not the author of this comment")

    if payload.content is not None:
        comment.content = payload.content

    db.commit()
    db.refresh(comment)
    return comment

@router.delete("/comments/{comment_id}", response_model=CommentRead)
def delete_comment(comment_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")

    if comment.author_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not allowed")

    db.delete(comment)
    db.commit()
    return comment