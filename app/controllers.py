from flask import jsonify, request
from app import app, services, validators
from app.repositories import Weather

@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    type_degrees = request.args.get('type_degrees')
    weather = Weather.get_by_city(city, "celsius" if type_degrees is None else type_degrees)
    return jsonify({"weather": weather})