import requests
import json
from datetime import datetime

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
        )

    return res
