from flask import Flask
from config import FlaskConfig
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(FlaskConfig)
CORS(app, supports_credentials=True)


from app import controllers