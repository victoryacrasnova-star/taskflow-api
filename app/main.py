from fastapi import FastAPI

from app.routers import auth, projects, task

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(auth.router)
app.include_router(projects.router)
app.include_router(task.router)
