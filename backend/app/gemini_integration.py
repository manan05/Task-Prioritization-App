import requests

class GeminiAPI:
    @staticmethod
    def summarize_tasks(tasks):
        url = "https://gemini-api/summarize"
        response = requests.post(url, json={"tasks": tasks})
        return response.json()
