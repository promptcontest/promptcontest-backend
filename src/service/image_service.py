from src.service.firestore_service import FirestoreService


class ImageService(FirestoreService):

    def __init__(self):
        super().__init__('images')


