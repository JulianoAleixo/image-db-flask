import uuid
from datetime import datetime
from app import db

class ImageModel:
    collection = db.collection('images')

    @classmethod
    def create(cls, filename, imageBase64):
        doc_id = str(uuid.uuid4())
        cls.collection.document(doc_id).set({
            'filename': filename,
            'imageBase64': imageBase64,
            'timestamp': datetime.now()
        })
        return doc_id

    @classmethod
    def get_all(cls):
        docs = cls.collection.stream()
        return [{**doc.to_dict(), 'id': doc.id} for doc in docs]

    @classmethod
    def get_by_id(cls, doc_id):
        doc = cls.collection.document(doc_id).get()
        if doc.exists:
            return {**doc.to_dict(), 'id': doc.id}
        return None

    @classmethod
    def update(cls, doc_id, filename=None, imageBase64=None):
        data = {}
        if filename:
            data['filename'] = filename
        if imageBase64:
            data['imageBase64'] = imageBase64
        if data:
            cls.collection.document(doc_id).update(data)
            return True
        return False

    @classmethod
    def delete(cls, doc_id):
        cls.collection.document(doc_id).delete()
        return True
