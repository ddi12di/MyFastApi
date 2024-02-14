from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from model.database import get_db
from conroller import crud
from model.schemas import UserPydantic, UserCreate

controller_user_router = APIRouter(prefix='/api/controller')


@controller_user_router.post("/create")
async  def create_user_service(request: UserCreate, db: Session = Depends(get_db)):
    created_user = crud.create_user(db, user=request)
    return created_user


@controller_user_router.patch("/update/{user_id}")
async  def update_user(request: UserPydantic, db: Session = Depends(get_db)):
    update_user = crud.update_user(db, user_id=request.id, username=request.username,
                                   phone_number=request.phone_number)
    return update_user

@controller_user_router.delete("/delete/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    crud.remove_user(db, user_id=user_id)
    return 200
