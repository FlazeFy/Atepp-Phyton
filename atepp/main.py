from fastapi import FastAPI
from modules.project.routers.project_handler import router

app = FastAPI()

# Router
app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI + Firestore example!"}

__all__ = ['app']
