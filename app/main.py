from fastapi import FastAPI
import model 
from config import engine
import router

model.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get('/')
async def home():
    return "Welcome home!"

app.include_router(router.router,prefix="/user", tags=["user"])