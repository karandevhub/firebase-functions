from pymongo import MongoClient
from app.config.settings import Config

client = None
db = None

def connect_db():
    global client, db
    try:
        client = MongoClient(Config.MONGO_URI)
        db = client[Config.DB_NAME]
        print("Connected to MongoDB")
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")


def get_db():
    if db is None:
        raise Exception("Database connection is not established. Call `connect_db` first.")
    return db
