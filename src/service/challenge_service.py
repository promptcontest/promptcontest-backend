from src.service.firestore_service import FirestoreService
from pydantic import BaseModel
from datetime import datetime, timedelta


ACTIVE = 'ACTIVE'
CLOSED = 'CLOSED'


class Challenge(BaseModel):
    name: str
    start: datetime
    end: datetime = None
    state: str = 'ACTIVE'


class ChallengeService(FirestoreService):

    def __init__(self):
        super().__init__('challenge')

    def create_new_challenge(self, name: str, start: datetime = None, end: datetime = None):

        if start is None:
            start = datetime.now()

        if end is None:
            end = start + timedelta(days=1)

        current_challenge = self.get_current_challenge()

        # TODO: we should close the challenge based on end data and then
        self.close_challenge(current_challenge.id)

        new_challenge = Challenge(name=name, start=start, end=end, state=ACTIVE)

        try:
            new_challenge = self.add(new_challenge.dict())
        except Exception as e:
            print(e)
            return None

        return new_challenge.dict()

    def get_current_challenge(self):
        result = self.collection.where('state', '==', ACTIVE).get()

        if len(result) == 0:
            return None

        if len(result) > 1:
            raise Exception('More than one active challenge')

        return [doc for doc in result][0]

    def close_challenge(self, challenge_id: str):

        # TODO: calculate winners for the previous challenge

        self.collection.document(challenge_id).update({'state': CLOSED, 'end': datetime.now()})