from fastapi import APIRouter, HTTPException
from modules.project.repositories.queries_folder import get_all_folder, get_folder_endpoint

router_folder = APIRouter()

# GET Query
@router_folder.get("/api/v3/folder", response_model=dict)
async def get_all_folder_v3():
    try:
        return get_all_folder()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router_folder.get("/api/v3/folder/endpoint/{id}", response_model=dict)
async def get_folder_endpoint_v3(id:str):
    try:
        return get_folder_endpoint(id=id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))