from app.repositories import WeatherRepository
from config import WeatherConfig

class WeatherService:
	@staticmethod
	def get_weather_by_city(city, type_degrees):
		type_degrees = WeatherConfig.CLIMATE_DEAFULT if type_degrees is None else type_degrees
		return WeatherRepository.get_by_city(city, type_degrees)