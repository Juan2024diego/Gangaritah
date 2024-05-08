from flask import jsonify, request
from app import app, validators
from app.services import WeatherService
import os
from dotenv import load_dotenv
load_dotenv()


@app.route('/weather')
def get_weather():
    if request.args.get('apikey') == os.getenv("API_KEY"):
        city = request.args.get('city')
        units = request.args.get('units')
        return jsonify({"weather": WeatherService.get_weather_by_city(city, units)})