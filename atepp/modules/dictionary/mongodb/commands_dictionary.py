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

def create_dct_md(dct_data):
    query = {
        "created_by": dct_data.created_by,
        "dictionary_type": dct_data.dictionary_type,
        "dictionary_name": dct_data.dictionary_name
    }
    docs = list(db_mongo.dictionaries.find(query))

    if not docs:
        result = db_mongo.dictionaries.insert_one(dct_data.dict())
        
        return {
            "id": str(result.inserted_id),
            "message": "Dictionaries added to MongoDB successfully"
        }
    else:
        return {
            "message": "Dictionary failed to add to MongoDB: Data already exists"
        }
