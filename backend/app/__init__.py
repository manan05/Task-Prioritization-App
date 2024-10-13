# app/__init__.py

from flask import Flask
from .config import Config
from .routes import app as routes_blueprint
from .database import MongoDB

# Initialize Flask app
app = Flask(__name__)

# Load configuration from config.py
app.config.from_object(Config)

# Initialize MongoDB connection
mongodb = MongoDB()

# Register blueprints for routing (if using Flask blueprints)
app.register_blueprint(routes_blueprint)

# You can add more initializations here (like logging or error handling)
