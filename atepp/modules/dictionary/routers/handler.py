from fastapi import APIRouter, HTTPException
from modules.dictionary.models.dictionary import Dictionary
from modules.dictionary.firestore.commands_dictionary import create_dct_fs
from modules.dictionary.firestore.queries_dictionary import get_my_variable_fs
from modules.dictionary.mongodb.commands_dictionary import create_dct_md
from modules.dictionary.mongodb.queries_dictionary import get_my_variable_md

router_dct = APIRouter()

# GET Query
@router_dct.get("/api/v1/dictionary/variable/{id}", response_model=dict)
async def get_my_variable_v1(id: str):
    try:
        return get_my_variable_fs(userId=id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router_dct.get("/api/v2/dictionary/variable/{id}", response_model=dict)
async def get_all_my_variable_v2(id: str):
    try:
        return get_my_variable_md(userId=id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# POST Command
@router_dct.post("/api/dictionary", response_model=dict)
async def create_dct(data: Dictionary):
    try:
        return {
            "command_firebase": create_dct_fs(data), 
            "command_mongodb": create_dct_md(data)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))