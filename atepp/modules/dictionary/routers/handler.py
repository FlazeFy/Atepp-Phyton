from fastapi import APIRouter, HTTPException
from modules.dictionary.models.dictionary import Dictionary
from modules.dictionary.firestore.commands_dictionary import create_dct_fs
from modules.dictionary.mongodb.commands_dictionary import create_dct_md

router_dct = APIRouter()

@router_dct.post("/api/dictionary", response_model=dict)
async def create_dct(data: Dictionary):
    try:
        return {
            "command_firebase": create_dct_fs(data), 
            "command_mongodb": create_dct_md(data)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))