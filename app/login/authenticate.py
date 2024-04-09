from config import SessionLocal
from model import User

def authenticate_user(session, username, password):
    user = session.query(User).filter_by(username=username).first()
    if user:
        if user.check_password(password):
            return user
    return None