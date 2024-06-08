from google.cloud import firestore
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "configs/atepp-cc0b7-firebase-adminsdk-70a8h-e0c72d879c.json"
db = firestore.Client()

def create_dct_fs(dct_data):
    dictionaries_ref = db.collection("dictionaries")
    query = dictionaries_ref.where("created_by", "==", dct_data.created_by).where("dictionary_type", "==", dct_data.dictionary_type).where("dictionary_name", "==", dct_data.dictionary_name)
    docs = list(query.stream())

    if not docs:
        doc_ref = dictionaries_ref.document()
        doc_ref.set(dct_data.dict())
        
        return {
            "id": doc_ref.id, 
            "message": "Dictionary added to Firestore successfully"
        }
    else:
        return { 
            "message": "Dictionary failed to add to Firestore: Data already exists"
        }
