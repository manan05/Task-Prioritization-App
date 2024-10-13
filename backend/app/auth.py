from flask import request, jsonify
from google_auth_oauthlib.flow import InstalledAppFlow
from .config import Config

def google_oauth():
    flow = InstalledAppFlow.from_client_secrets_file(Config.GOOGLE_CLIENT_SECRET_FILE, scopes=['https://www.googleapis.com/auth/calendar'])
    credentials = flow.run_local_server(port=8080)
    return credentials
