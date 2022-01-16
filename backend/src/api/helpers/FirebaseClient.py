import pyrebase


class FirebaseClient:
    def __init__(self):
        config = {
            "apiKey": "AIzaSyDfzIpFWkzgemD9fEWeZJED7RXlGgwCSWw",
            "authDomain": "disaster-recovery-nw.firebaseapp.com",
            "databaseURL": "https://disaster-recovery-nw-default-rtdb.firebaseio.com",
            "storageBucket": "disaster-recovery-nw.appspot.com"
        }
        self.firebase = pyrebase.initialize_app(config)
        self.db = self.firebase.database()

    def get_db(self):
        return self.db
