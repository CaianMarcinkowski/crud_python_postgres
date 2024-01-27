from sqlalchemy.orm import Session
from model import users
from schema import usersSchema

def get_users(db:Session, skip:int=0, limit=100):
    return db.query(users).offset(skip).limit(limit).all()

def get_user_by_id(db:Session,user_id: int):
    return db.query(users).filter(users.id == user_id).first()

def create_user(db: Session, user: usersSchema):
    _user = users(username=user.username, email=user.email, password=user.password)
    db.add(_user)
    db.commit()
    db.refresh(_user)
    return _user

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