from fastapi import APIRouter, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schema import RequestUsers, Response
from login.authenticate import authenticate_user
from flask import session
import crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/create')
async def create_user(request: RequestUsers, db: Session = Depends(get_db)):
    username = request.parameter.username
    email = request.parameter.email
    password = request.parameter.password
    crud.create_user(db, username, email, password)
    return Response(code="200", status="Ok", message="User created successfully")

@router.get('/')
async def get_users(db: Session=Depends(get_db)):
    _user = crud.get_users(db,0,100)
    return Response(code="200", status="Ok", message="Users retrieved successfully", result=_user).dict(exclude_none=True)

@router.get('/{id}')
async def get_user_by_id(id:int, db:Session = Depends(get_db)):
    _user = crud.get_user_by_id(db,id)
    return Response(code="200", status="Ok", message="User retrieved successfully", result=_user).dict(exclude_none=True)

@router.post('/update')
async def update_user(request: RequestUsers, db:Session = Depends(get_db)) :
    _user = crud.update_user(db, user_id=request.user.id, username=request.user.username, password=request.user.password, email=request.user.email)
    return Response(code="200", status="Ok", message="Successfully updated", result=_user).dict(exclude_none=True)

@router.delete('/{id}')
async def delete_user(id:int, db:Session = Depends(get_db)):
    crud.remove_user(db, id)
    return Response(code="200", status="Ok", message="Successfully deleted").dict(exclude_none=True)

@router.post('/login')
async def login(request: RequestUsers, db:Session = Depends(get_db)):
    _user = authenticate_user(db, username=request.parameter.username, password=request.parameter.password)
    if _user is None:
        return Response(code="401", status="Failed", message="Login or pass incorrect").dict(exclude_none=True)
    else:
        return Response(code="200", status="Ok", message="Successfully login").dict(exclude_none=True)

@router.post('/protected')
async def protected(request: RequestUsers, db:Session = Depends(get_db)):
    _user = authenticate_user(db, username=request.parameter.username, password=request.parameter.password)
    if _user in session:
        return Response(code="200", status="Ok", message="Successfully protected").dict(exclude_none=True)
    else:
        return Response(code="401", status="", message="Unauthorized").dict(exclude_none=True)
    