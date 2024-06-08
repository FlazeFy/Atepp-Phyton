from google.cloud import firestore
import os
from pymongo import MongoClient
import json
from typing import Final

with open('configs/mongodb.json', 'r') as config_file:
    config = json.load(config_file)
TOKEN: Final = config['TOKEN']

client = MongoClient(TOKEN)
db_mongo = client.test_database

def get_all_my_project_md(userId):
    query = {
        "created_by": userId,
        "deleted_at": None
    }
    select = {
        "_id": 1,
        "id":1,
        "project_slug": 1,
        "project_title": 1,
        "project_category": 1,
        "project_type": 1,
        "created_at": 1,
        "project_desc": 1
    }

    docs = list(db_mongo.projects.find(query, select))

    for doc in docs:
        doc["_id"] = str(doc["_id"])

    if docs:
        return {
            "data": docs,
            "message": "Projects found",
            "count": len(docs)
        }
    else:
        return {
            "data": [],
            "message": "No projects found",
            "count": 0
        }
