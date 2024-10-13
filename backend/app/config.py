import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    CANVAS_ACCESS_TOKEN = os.getenv("CANVAS_ACCESS_TOKEN")
    GOOGLE_CLIENT_SECRET_FILE = os.getenv("GOOGLE_CLIENT_SECRET_FILE")
    MONGO_URI = os.getenv("MONGO_URI")
