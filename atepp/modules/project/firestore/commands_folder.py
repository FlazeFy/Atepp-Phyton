from google.cloud import firestore
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "configs/atepp-cc0b7-firebase-adminsdk-70a8h-e0c72d879c.json"
db = firestore.Client()

def create_folder_fs(folder_data):
    doc_ref = db.collection("folders").document()
    doc_ref.set(folder_data.dict())
    
    return {
        "id": doc_ref.id, 
        "project_id": folder_data.project_id, 
        "message": "Folder added to Firestore successfully"
    }
