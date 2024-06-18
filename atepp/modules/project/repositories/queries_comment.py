from configs.configs import con
from sqlalchemy import select, desc, and_, func
from modules.project.models.comment import model_all_comment
from modules.endpoint.models.models_endpoint import model_all_endpoint
from modules.user.models.models_user import user

def get_comment_by_endpoint_ctx(endpoint:str, ctx:str):
    # Query builder
    query = select(
        model_all_comment.c.comment_context,
        model_all_comment.c.comment_body, 
        model_all_comment.c.comment_attachment, 
        model_all_comment.c.created_at, 
        user.c.username.label('created_by')
    ).join(
        model_all_endpoint, model_all_endpoint.c.id == model_all_comment.c.endpoint_id
    ).join(
        user, user.c.id == model_all_comment.c.created_by
    ).where(
        and_(
            model_all_comment.c.comment_context == ctx,
            model_all_comment.c.endpoint_id == endpoint
        )
    ).order_by(
        model_all_comment.c.created_at
    )

    # Exec
    result = con.execute(query)
    data = result.fetchall()
    data_list = [dict(row._mapping) for row in data]

    if data_list:
        return {
            "data": data_list,
            "message": "Comment found",
            "count": len(data)
        }
    else:
        return {
            "message": "No comment found",
        }
    
def get_all_comment():
    # Query builder
    query = select(
        model_all_comment.c.comment_context,
        model_all_comment.c.comment_body, 
        model_all_comment.c.comment_attachment, 
        model_all_comment.c.created_at, 
        model_all_endpoint.c.endpoint_name, 
        model_all_endpoint.c.endpoint_url, 
        user.c.username.label('created_by')
    ).join(
        model_all_endpoint, model_all_endpoint.c.id == model_all_comment.c.endpoint_id
    ).join(
        user, user.c.id == model_all_comment.c.created_by
    ).order_by(
        model_all_endpoint.c.endpoint_name,
        model_all_comment.c.created_at
    )

    # Exec
    result = con.execute(query)
    data = result.fetchall()
    data_list = [dict(row._mapping) for row in data]

    if data_list:
        return {
            "data": data_list,
            "message": "Comment found",
            "count": len(data)
        }
    else:
        return {
            "message": "No comment found",
        }