from configs.configs import con
from sqlalchemy import select, desc, and_, func
from modules.project.models.folder import model_all_folder
from modules.project.models.project import model_all_project
from modules.endpoint.models.models_endpoint import model_all_endpoint
from modules.user.models.models_user import user

def get_all_folder():
    # Query builder
    query = select(
        model_all_folder.c.id,
        model_all_folder.c.folder_name,
        model_all_folder.c.folder_slug, 
        model_all_folder.c.folder_desc, 
        model_all_project.c.project_title, 
        user.c.username.label('created_by')
    ).join(
        model_all_project, model_all_project.c.id == model_all_folder.c.project_id
    ).join(
        user, user.c.id == model_all_folder.c.created_by
    ).order_by(
        model_all_folder.c.folder_name,
        model_all_folder.c.created_at
    )

    # Exec
    result = con.execute(query)
    data = result.fetchall()
    data_list = [dict(row._mapping) for row in data]

    if data_list:
        return {
            "data": data_list,
            "message": "folder found",
            "count": len(data)
        }
    else:
        return {
            "message": "No folder found",
        }
    
def get_folder_endpoint(id:str):
    # Query builder
    query = select(
        model_all_folder.c.folder_name,
        model_all_folder.c.folder_slug, 
        model_all_endpoint.c.endpoint_name,
        model_all_endpoint.c.endpoint_url,
        model_all_endpoint.c.endpoint_desc,
        model_all_endpoint.c.endpoint_method,
        model_all_project.c.project_title, 
        user.c.username.label('created_by')
    ).join(
        model_all_project, model_all_project.c.id == model_all_folder.c.project_id
    ).join(
        model_all_endpoint, model_all_endpoint.c.folder_id == model_all_folder.c.id
    ).join(
        user, user.c.id == model_all_folder.c.created_by
    ).where(
        and_(
            model_all_folder.c.id == id
        )
    ).order_by(
        model_all_project.c.project_title, 
        model_all_endpoint.c.endpoint_name,
        model_all_folder.c.folder_name,
        model_all_folder.c.created_at
    )

    # Exec
    result = con.execute(query)
    data = result.fetchall()
    data_list = [dict(row._mapping) for row in data]

    if data_list:
        return {
            "data": data_list,
            "message": "endpoint found",
            "count": len(data)
        }
    else:
        return {
            "message": "No endpoint found",
        }