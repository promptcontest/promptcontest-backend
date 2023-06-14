from src.service.firestore_service import FirestoreService
from pydantic import BaseModel
import datetime
from firebase_admin import firestore


class Image(BaseModel):
    user_id: str
    twitter_handle: str
    image_url: str
    timestamp: str = datetime.datetime.now()
    rank: int = 0
    upvotes: int = 0
    downvotes: int = 0


class ImageService(FirestoreService):

    def __init__(self):
        super().__init__('challenge')

    def get_challenge_images(self, challenge_id: str):

        result = self.collection.document(challenge_id).collection('images').order_by('rank').get()

        if len(result) == 0:
            return None

        return [doc for doc in result]

    def add_image(self, challenge_id: str, image: Image):
        ref = self.collection.document(challenge_id).collection('images')

        try:
            new_image = ref.add(image.dict())[1]
        except Exception as e:
            print(e)
            return None

        return new_image

    def upvote_image(self, challenge_id: str, image_id: str):
        ref = self.collection.document(challenge_id).collection('images').document(image_id)
        ref.update({'upvotes': firestore.Increment(1)})

        result = ref.get()

        return result

    def downvote_image(self, challenge_id: str, image_id: str):
        ref = self.collection.document(challenge_id).collection('images').document(image_id)
        ref.update({'downvotes': firestore.Increment(1)})

        result = ref.get()

        return result