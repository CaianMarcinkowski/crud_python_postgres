from sqlalchemy.orm import Session
from model import User
from schema import usersSchema
import bcrypt

def get_users(db:Session, skip:int=0, limit=100):
    return db.query(User).offset(skip).limit(limit).all()

def get_user_by_id(db:Session,user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, username: str, email: str, password: str):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    db_user = User(username=username, email=email, password=hashed_password.decode('utf-8'))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def remove_user(db:Session, user_id: int):
    _user = get_user_by_id(db=db, user_id=user_id)
    db.delete(_user)
    db.commit()

def update_user(db:Session, user_id: int, username:str, password:str, email:str):
    _user = get_user_by_id(db=db, user_id=user_id)
    _user.username = username
    _user.password = password
    _user.email = email
    db.commit()
    db.refresh(_user)
    return _user