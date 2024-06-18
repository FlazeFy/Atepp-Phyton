import requests
import json
from datetime import datetime
from configs.configs import con
from sqlalchemy import select, desc, and_, func
from modules.project.models.project import model_all_project
from modules.endpoint.models.models_endpoint import model_all_endpoint
from modules.user.models.models_user import user

base_url = 'http://127.0.0.1:8000'
headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer 132|5Nyu0gn75gi0tQ48ZgKCI1Yiqg1xF57hrlRfmKTB3dccb1a0', 
}

async def get_all_my_project():
    response = requests.get(base_url+'/api/v1/project/detail', headers=headers)
    data = response.content
    json_data = json.loads(data.decode('utf-8'))

    res = ''    
    for dt in json_data['data']:
        created_at_str = dt['created_at'][:-10] 
        created_at_dt = datetime.strptime(created_at_str, '%Y-%m-%dT%H:%M:')

        res += (
            f"- **{dt['project_title']}**\n"
            f"Category: {dt['project_category']}\n"
            f"Created At: {created_at_dt.strftime('%d %B %Y %H:%M')}\n"
            f"Total Endpoint: {dt['total_endpoint']}\n\n"
            f"**About Project**\n{dt['project_desc'] if dt['project_desc'] else '*No Description Provided*'}\n\n"
            f"**Show Endpoint :** \n"
            f"```\n{dt['project_slug']+'/endpoint'}```\n"
            f"**Project Detail :** \n"
            f"```\n{dt['project_slug']+'/detail'}```\n\n"
        )

    return res

async def get_endpoint_by_project(slug):
    response = requests.get(base_url+'/api/v1/project/endpoint/project/'+slug, headers=headers)
    data = response.content
    json_data = json.loads(data.decode('utf-8'))

    res = ''    
    folder_before = ''

    for dt in json_data['data']:
        if folder_before == '' or folder_before != dt['folder_name']:
            res += f"**{'========== + Folder '+dt['folder_name']+' + ==========' if dt['folder_name'] else '*========== + No Folder + ==========*'}**\n\n"
            folder_before = dt['folder_name']

        res += (
            f"- **{dt['endpoint_method']}** | **{dt['endpoint_name']}**\n"
            f"URL: \n{dt['endpoint_url']}\n"
            f"**Description : **\n{dt['endpoint_desc'] if dt['endpoint_desc'] else '*No Description Provided*'}\n\n"
            f"**Show Endpoint's Run History :** \n"
            f"```\n{dt['id']+'/history/run'}```\n"
            f"**Show Endpoint's Test History :** \n"
            f"```\n{dt['id']+'/history/test'}```\n"
        )

    return res if res != '' else '*No Endpoint Found!*'

async def get_history_run_endpoint(id):
    response = requests.get(base_url+'/api/v1/project/response/'+id, headers=headers)
    data = response.content
    json_data = json.loads(data.decode('utf-8'))

    res = ''    
    date_before = ''

    for dt in json_data['data']:
        created_at_str = dt['created_at']
        created_at_dt = datetime.strptime(created_at_str, '%Y-%m-%d %H:%M:%S')

        if date_before == '' or date_before != created_at_dt.strftime('%d %B %Y'):
            res += f"** ========== + {created_at_dt.strftime('%d %B %Y')} + ========== **\n\n"
            date_before = created_at_dt.strftime('%d %B %Y')

        res += (
            f"- **{dt['response_method']}** | **Status : {dt['response_status']}** | **{round(dt['response_time'], 3)} ms**\n"
            f"On **{dt['endpoint_name']}** from {dt['response_env']}\n"
            f"**Response Body :** \n"
            f"```\n{dt['id']+'/response/body'}```\n"
        )

    return res if res != '' else '*No History Found!*'

def get_all_project():
    # Query builder
    query = select(
        model_all_project.c.id,
        model_all_project.c.project_slug, 
        model_all_project.c.project_title, 
        model_all_project.c.project_category, 
        model_all_project.c.project_type,
        model_all_project.c.project_desc,
        model_all_project.c.created_at,
        user.c.username,
        func.count(model_all_endpoint.c.id).label('total_endpoint')
    ).outerjoin(
        model_all_endpoint, model_all_endpoint.c.project_id == model_all_project.c.id
    ).join(
        user, user.c.id == model_all_project.c.created_by
    ).where(
        model_all_project.c.deleted_at.is_(None)
    ).group_by(
        model_all_project.c.id
    ).order_by(
        desc(model_all_project.c.created_at),
        desc(model_all_project.c.project_title),
    )

    # Exec
    result = con.execute(query)
    data = result.fetchall()
    data_list = [dict(row._mapping) for row in data]

    if data_list:
        return {
            "data": data_list,
            "message": "Projects found",
            "count": len(data)
        }
    else:
        return {
            "message": "No projects found",
        }


