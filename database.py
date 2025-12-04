# database.py
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)
db = client["hexa_ai"]
waitlist_collection = db["waitlistt"]
