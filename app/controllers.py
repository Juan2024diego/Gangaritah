from flask import jsonify, request
from app import app, validators
from app.services import WeatherService


@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    type_degrees = request.args.get('type_degrees')
    return jsonify({"weather": WeatherService.get_weather_by_city(city, type_degrees)})