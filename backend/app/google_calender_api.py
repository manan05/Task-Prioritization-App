import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from .config import Config

class GoogleCalendarAPI:
    SCOPES = ['https://www.googleapis.com/auth/calendar']

    def __init__(self):
        self.credentials = self.get_credentials()

    def get_credentials(self):
        flow = InstalledAppFlow.from_client_secrets_file(Config.GOOGLE_CLIENT_SECRET_FILE, self.SCOPES)
        credentials = flow.run_local_server(port=8080)
        with open("token.pkl", "wb") as token:
            pickle.dump(credentials, token)
        return credentials

    def get_calendar_service(self):
        return build("calendar", "v3", credentials=self.credentials)
    
    def get_events(self):
        service = self.get_calendar_service()
        return service.calendarList().list().execute()
