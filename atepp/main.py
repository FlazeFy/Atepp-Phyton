from fastapi import FastAPI
from modules.project.routers.project_handler import router_project
from modules.dictionary.routers.handler import router_dct
from modules.project.routers.comment_handler import router_comment
from modules.project.routers.folder_handler import router_folder
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:2000",
    "http://localhost:8000",
    "http://localhost:5173",
    "http://127.0.0.1",
    "http://127.0.0.1:8080",
    "http://127.0.0.1:2000",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Router
app.include_router(router_project)
app.include_router(router_dct)
app.include_router(router_comment)
app.include_router(router_folder)

@app.get("/")
async def root():
    return {"message": "Welcome to Atepp, API Testing App, Test your API, Make dummy data, Generate document, and share it with your co-worker"}

__all__ = ['app']
