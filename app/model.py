from sqlalchemy import Column, Integer, String
from config import Base

class users(Base):
        __tablename__ = 'users'
        id = Column(Integer, primary_key=True)
        username = Column(String(255))
        password = Column(String(255))
        email = Column(String(255))