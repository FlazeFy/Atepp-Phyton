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

def create_folder_md(folder_data):
    result = db_mongo.folders.insert_one(folder_data.dict())
    
    return {
        "id": str(result.inserted_id),
        "project_id": folder_data.project_id, 
        "message": "Folder added to MongoDB successfully"
    }
