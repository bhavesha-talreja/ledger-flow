from fastapi import FastAPI
from app.database import engine, Base
from app.models.users import User

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}