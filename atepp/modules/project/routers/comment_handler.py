from fastapi import APIRouter, HTTPException
from modules.project.repositories.queries_comment import get_comment_by_endpoint_ctx, get_all_comment

router_comment = APIRouter()

# GET Query (Admin)
@router_comment.get("/api/v3/comment/by/{endpoint}/{ctx}", response_model=dict)
async def get_comment_by_endpoint_ctx_v3(endpoint:str, ctx:str):
    try:
        return get_comment_by_endpoint_ctx(endpoint=endpoint, ctx=ctx)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router_comment.get("/api/v3/comment/all", response_model=dict)
async def get_all_comment_v3():
    try:
        return get_all_comment()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))