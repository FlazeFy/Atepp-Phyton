from google.cloud import firestore
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "configs/atepp-cc0b7-firebase-adminsdk-70a8h-e0c72d879c.json"
db = firestore.Client()

def create_project_fs(project_data):
    doc_ref = db.collection("projects").document()
    doc_ref.set(project_data.dict())
    return {
        "id": doc_ref.id, 
        "message": "Project added to Firestore successfully"
    }
