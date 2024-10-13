import requests
from urllib.parse import urlencode
from .config import Config

class CanvasAPI:
    BASE_URL = "https://uta.instructure.com/api/v1"

    @staticmethod
    def get_headers():
        return {'Authorization': f'Bearer {Config.CANVAS_ACCESS_TOKEN}'}
    
    @classmethod
    def get_colors(cls):
        url = f"{cls.BASE_URL}/users/self/colors"
        response = requests.get(url, headers=cls.get_headers())
        return response.json()

    @classmethod
    def get_calendar_events(cls, start_date, end_date, context_codes):
        params = {
            'start_date': start_date,
            'end_date': end_date,
            'context_codes[]': context_codes,
            'per_page': 50
        }
        encoded_params = urlencode(params, doseq=True)
        full_url = f"{cls.BASE_URL}/calendar_events?{encoded_params}"
        response = requests.get(full_url, headers=cls.get_headers())
        return response.json() if response.status_code == 200 else None
