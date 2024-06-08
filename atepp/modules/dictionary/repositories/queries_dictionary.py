import requests
import json
from datetime import datetime

base_url = 'http://127.0.0.1:8000'
headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer 132|5Nyu0gn75gi0tQ48ZgKCI1Yiqg1xF57hrlRfmKTB3dccb1a0', 
}

async def get_my_dictionary(currentPage:int):
    response = requests.get(f"{base_url}/api/v1/dictionary/variable?page={currentPage}", headers=headers)
    data = response.content
    json_data = json.loads(data.decode('utf-8'))

    total_page = json_data['data']['last_page']
    items_per_page = json_data['data']['per_page']
    items = json_data['data']['data']

    res = ''    
    for dt in items:
        res += (
            f"**- {dt['dictionary_name']}**"
            f"```{dt['dictionary_value']}```\n"
        )

    return [res, total_page, items_per_page]