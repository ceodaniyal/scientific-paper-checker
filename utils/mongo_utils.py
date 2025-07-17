from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client["paper_checker"]
collection = db["reviews"]

def save_review_to_mongo(paper_id, data):
    collection.insert_one({"_id": paper_id, **data})
