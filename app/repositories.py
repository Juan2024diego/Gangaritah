from app.models import CityWeather
from app.data import cities, users


class WeatherRepository:
	@staticmethod
	def get_by_city(city, units):
		search = [item for item in cities if item['name'] == city]
		if len(search) > 0:
			return CityWeather(
				search[0]["name"],
				search[0]["weather"][0]["main"],
				search[0]["main"]["temp"],
				search[0]["main"]["humidity"],
				search[0]["wind"]["speed"],
				units
			).to_json()


class UserRepository:

	@staticmethod
	def login(user):
		print("$$$$$##############################", users[0]["password"])
		search = [item for item in users if item['email'] == user.email and item['password'] == user.password]
		if len(search) > 0:
			return {"logged": True, "status": "Successful authentication"}
		return {"logged": False, "status": "Invalid username or password"}