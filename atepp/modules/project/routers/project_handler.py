from fastapi import APIRouter, HTTPException
from modules.project.models.project import Project
from modules.project.firestore.commands_project import create_project_fs
from modules.project.mongodb.commands_project import create_project_md

router = APIRouter()

@router.post("/items/", response_model=dict)
async def create_item(project: Project):
    try:
        return {
            "command_firebase": create_project_fs(project), 
            "command_mongodb": create_project_md(project)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))