from app.repositories import WeatherRepository
from config import WeatherConfig
from app.helpers import Helpers


class WeatherService:
	@staticmethod
	def get_weather_by_city(city, units):
		units = WeatherConfig.CLIMATE_DEAFULT if units is None else units
		return WeatherRepository.get_by_city(Helpers.normalize_string(city), units)