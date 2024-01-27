from fastapi import APIRouter, HTTPException, Path, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schema import usersSchema, RequestUsers, Response
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
    crud.create_user(db, user=request.parameter)
    return Response(code="200", status="Ok", message="User created successfully").dict(exclude_none=True)

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
