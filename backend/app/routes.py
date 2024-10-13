from flask import Flask, jsonify
from .canvas_api import CanvasAPI
from .google_calendar_api import GoogleCalendarAPI
from .gemini_integration import GeminiAPI

app = Flask(__name__)

@app.route('/events/consolidate', methods=['GET'])
def consolidate_events():
    canvas_events = CanvasAPI.get_calendar_events('2024-09-29', '2024-11-03', ['course_192508'])
    google_events = GoogleCalendarAPI().get_events()
    
    consolidated = {"canvas_events": canvas_events, "google_events": google_events}
    summary = GeminiAPI.summarize_tasks(consolidated)
    return jsonify(summary)
