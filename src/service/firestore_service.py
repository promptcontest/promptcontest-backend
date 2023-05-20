# services/firebase_service.py
from abc import ABC, abstractmethod
from src.firebase_app import db


class FirestoreService(ABC):

    def __init__(self, collection_name):
        self.db = db
        self.collection = self.db.collection(collection_name)

    def add(self, data: dict):
        doc_ref = self.collection.document()
        doc_ref.set(data)
        return doc_ref

    def get(self, filters: dict = None):
        collection_ref = self.collection
        if filters:
            for key, value in filters.items():
                collection_ref = collection_ref.where(key, '==', value)
        docs = collection_ref.stream()
        return [doc.to_dict() for doc in docs]

    # Any additional common database operations can be added here as needed.
