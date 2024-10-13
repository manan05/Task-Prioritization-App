from pymongo import MongoClient
from .config import Config

class MongoDB:
    def __init__(self):
        self.client = MongoClient(Config.MONGO_URI)
        self.db = self.client['task_db']

    def insert_task_summary(self, summary):
        return self.db.summaries.insert_one(summary)

    def get_task_summaries(self):
        return self.db.summaries.find()
