from google.cloud import firestore
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "configs/atepp-cc0b7-firebase-adminsdk-70a8h-e0c72d879c.json"
db = firestore.Client()

def get_all_my_project_fs(userId):
    project_ref = db.collection('projects')
    query = (
        project_ref.where("created_by", "==", userId)
        .where("deleted_at", "==", None)
        .select(['id','project_slug', 'project_title', 'project_category', 'project_type', 'created_at', 'project_desc'])
    )
    docs = list(query.stream())

    if docs:
        sorted_docs = sorted([doc.to_dict() for doc in docs], key=lambda x: x['project_title'], reverse=False)
        filtered_docs = [
            {
                # "firestore_id": doc.id,
                "id": doc.get('id'),
                "project_slug": doc.get('project_slug'),
                "project_title": doc.get('project_title'),
                "project_category": doc.get('project_category'),
                "project_type": doc.get('project_type'),
                "created_at": doc.get('created_at'),
                "project_desc": doc.get('project_desc')
            }
            for doc in sorted_docs
        ]
        return {
            "data": filtered_docs,
            "message": "Projects found",
            "count": len(filtered_docs)
        }
    else:
        return {
            "message": "No projects found",
        }