from pymongo import MongoClient
from animal_dashboard.config import Config

class AnimalShelter:
    def __init__(self, username='aacuser', password='password'):
        # Replace this with your actual MongoDB connection setup
        self.client = MongoClient(f"mongodb://{username}:{password}@localhost:27017/?authSource=AAC")
        self.database = self.client['AAC']
        self.collection = self.database['animals']
        
    def read_all(self):
        """Returns all documents in the collection as a list"""
        return list(self.collection.find({}, {'_id': False}))  # Return without _id for Dash compatibility

    def create(self, data):
        return self.collection.insert_one(data)

    def read(self, query={}):
        return list(self.collection.find(query))

    def update(self, _id, update_data):
        return self.collection.update_one({'_id': _id}, {'$set': update_data})

    def delete(self, _id):
        return self.collection.delete_one({'_id': _id})
