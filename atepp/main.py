from fastapi import FastAPI
from modules.project.routers.project_handler import router

app = FastAPI()

# Router
app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Welcome to Atepp, API Testing App, Test your API, Make dummy data, Generate document, and share it with your co-worker"}

__all__ = ['app']
