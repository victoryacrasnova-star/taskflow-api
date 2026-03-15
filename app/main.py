from fastapi import FastAPI
from app.database import engine
from sqlalchemy import text

app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/test_db")
async def get_db():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
    return {"message": "Database Connected"}