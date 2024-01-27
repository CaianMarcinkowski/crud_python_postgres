from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')

class usersSchema(BaseModel):
    id: Optional[int]=None
    username: Optional[str]=None
    password: Optional[str]=None
    email: Optional[str]=None

    class Config:
        orm_mode = True

class RequestUsers(BaseModel):
    parameter: usersSchema

class Response (GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T] = None
