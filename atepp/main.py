from fastapi import FastAPI
from modules.project.routers.project_handler import router_project
from modules.dictionary.routers.handler import router_dct

app = FastAPI()

# Router
app.include_router(router_project)
app.include_router(router_dct)

@app.get("/")
async def root():
    return {"message": "Welcome to Atepp, API Testing App, Test your API, Make dummy data, Generate document, and share it with your co-worker"}

__all__ = ['app']
