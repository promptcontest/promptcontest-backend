from src.service.firestore_service import FirestoreService


class ImageService(FirestoreService):

    def __init__(self):
        super().__init__('images')

    def get_challenge_images(self, challenge_id: str):

        result = self.collection.where('challenge_id', '==', challenge_id).get()

        if len(result) == 0:
            return None

        return [doc for doc in result]