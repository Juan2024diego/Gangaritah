from app.models import CityWeather
from app.data import data


class Weather:
	@staticmethod
	def get_by_city(city, type_degrees):
		search = [item for item in data if item['name'] == city]
		if len(search) > 0:
			return CityWeather(
				search[0]["name"],
				search[0]["weather"][0]["main"],
				search[0]["main"]["temp"],
				search[0]["main"]["humidity"],
				search[0]["wind"]["speed"],
				type_degrees
			).to_json()
  