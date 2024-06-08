from google.cloud import firestore
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "configs/atepp-cc0b7-firebase-adminsdk-70a8h-e0c72d879c.json"
db = firestore.Client()

def get_my_variable_fs(userId):
    project_ref = db.collection('dictionaries')
    query = (
        project_ref.where("created_by", "==", userId)
        .where("dictionary_type","==","variable")
        .select(['id','dictionary_name','dictionary_value','created_at','updated_at'])
    )
    docs = list(query.stream())

    if docs:
        sorted_docs = sorted([doc.to_dict() for doc in docs], key=lambda x: x['created_at'], reverse=True)
        filtered_docs = [
            {
                # "firestore_id": doc.id,
                "id": doc.get('id'),
                "dictionary_name": doc.get('dictionary_name'),
                "dictionary_value": doc.get('dictionary_value'),
                "created_at": doc.get('created_at'),
                "updated_at": doc.get('updated_at')
            }
            for doc in sorted_docs
        ]
        return {
            "data": filtered_docs,
            "message": "Dictionaries found",
            "count": len(filtered_docs)
        }
    else:
        return {
            "message": "No Dictionaries found",
        }