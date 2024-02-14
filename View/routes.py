from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from model.database import get_db
from conroller import crud

view_user_router = APIRouter(prefix='/api/view')

@view_user_router.get("/")
async  def get_users(skip: int=0, limit: int = 199, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip, limit)
    return users


@view_user_router.get("/user/{user_id}")
async  def get_users_by_id(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_users(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

