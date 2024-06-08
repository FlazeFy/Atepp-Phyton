from google.cloud import firestore
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "configs/atepp-cc0b7-firebase-adminsdk-70a8h-e0c72d879c.json"
db = firestore.Client()

def create_project_fs(project_data):
    project_ref = db.collection('projects')
    query = project_ref.where("created_by","==",project_data.created_by).where("project_title","==",project_data.project_title)
    docs = list(query.stream())

    if not docs:
        doc_ref = project_ref.document()
        doc_ref.set(project_data.dict())
        
        return {
            "id": doc_ref.id, 
            "message": "Project added to Firestore successfully"
        }
    else:
        return { 
            "message": "Project failed to add to Firestore: Data already exists"
        }
