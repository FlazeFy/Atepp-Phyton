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

def create_project_md(project_data):
    query = {
        "created_by": project_data.created_by,
        "project_title": project_data.project_title
    }
    docs = list(db_mongo.projects.find(query))

    if not docs:
        result = db_mongo.projects.insert_one(project_data.dict())
        
        return {
            "id": str(result.inserted_id),
            "message": "Project added to MongoDB successfully"
        }
    else:
        return {
            "message": "Project failed to add to MongoDB: Data already exists"
        }
