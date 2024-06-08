from fastapi import APIRouter, HTTPException
from modules.project.models.project import Project
from modules.project.models.folder import Folder
from modules.project.firestore.commands_project import create_project_fs
from modules.project.firestore.commands_folder import create_folder_fs
from modules.project.mongodb.commands_project import create_project_md
from modules.project.mongodb.commands_folder import create_folder_md

router_project = APIRouter()

@router_project.post("/api/project", response_model=dict)
async def create_project(data: Project):
    try:
        return {
            "command_firebase": create_project_fs(data), 
            "command_mongodb": create_project_md(data)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router_project.post("/api/folder", response_model=dict)
async def create_folder(data: Folder):
    try:
        return {
            "command_firebase": create_folder_fs(data), 
            "command_mongodb": create_folder_md(data)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))