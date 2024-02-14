from sqlalchemy.orm import Session
from model.core import User
from model.schemas import UserCreate

def get_users(db: Session, skip: int = 0, limit: int=100):
    return db.query(User).offset(skip).limit(limit).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def create_user(db: Session, user: UserCreate):
    db_user = User(username=user.username, phone_number=user.phone_number)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def remove_user(db: Session, user_id: int):
    db_user = get_user_by_id(db=db, user_id=user_id)
    db.delete(db_user)
    db.commit()

def update_user(db: Session, user_id: int, username: str, phone_number: int):
    db_user = get_user_by_id(db=db, user_id=user_id)
    db_user.username = username
    db_user.phone_number = phone_number
    db.commit()
    db.refresh(db_user)
    return db_user