from fastapi import FastAPI
from app import models
from .database import engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()



@app.get("/")
async def home():
    return{"m":"hello"}