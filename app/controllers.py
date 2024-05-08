from flask import jsonify
from app import app, services, validators

@app.route('/weather/<city_name>')
def get_weather(city_name):
    return 'Weather App'