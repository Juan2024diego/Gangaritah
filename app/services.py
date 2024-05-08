from app.repositories import WeatherRepository, UserRepository
from config import WeatherConfig
from app.helpers import Helpers
from app.models import UserAuth


class WeatherService:
	@staticmethod
	def get_weather_by_city(city, units):
		units = WeatherConfig.CLIMATE_DEAFULT if units is None else units
		return WeatherRepository.get_by_city(Helpers.normalize_string(city), units)

class UserService:
	@staticmethod
	def login_user(user):
		return UserRepository.login(user)
