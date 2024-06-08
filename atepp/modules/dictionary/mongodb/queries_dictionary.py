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

def get_my_variable_md(userId):
    query = {
        "created_by": userId,
        "dictionary_type": "variable"
    }
    select = {
        "_id": 1,
        "id":1,
        "dictionary_name": 1,
        "dictionary_value": 1,
        "created_at": 1,
        "updated_at": 1
    }

    docs = list(db_mongo.dictionaries.find(query, select))

    for doc in docs:
        doc["_id"] = str(doc["_id"])

    if docs:
        return {
            "data": docs,
            "message": "Dictionaries found",
            "count": len(docs)
        }
    else:
        return {
            "message": "No dictionaries found",
        }
