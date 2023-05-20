import os
import sys
from pathlib import Path

import firebase_admin
from firebase_admin import credentials, firestore


def get_path_to_config(*paths):
    name = os.path.join(*paths)

    for p in [os.getcwd(), *sys.path]:
        to_explore = [p, *list(reversed(Path(p).parents))]
        for e in to_explore:
            ret = os.path.join(e, name)
            if os.path.exists(ret):
                return ret

    raise FileNotFoundError(f"{name} not found.")


firebase_key = get_path_to_config('firebase', 'promptcontest-356e0-firebase-adminsdk-7bwlz-4385e1fb00.json')
cred = credentials.Certificate(firebase_key)
firebase_app = firebase_admin.initialize_app(cred)
db = firestore.client()

