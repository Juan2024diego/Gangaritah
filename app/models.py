class CityWeather:


    def __init__(self, name, weather, temp, humidity, wind_speed, units):
        self.name = name
        self.weather = weather
        self.temp = temp
        self.humidity = humidity
        self.wind_speed = wind_speed
        self.units = units
    

    def to_json(self):
        weather = {
                "name": self.name,
                "weather": self.weather,
                "humidity": self.humidity,
                "wind_speed": self.wind_speed
            }
        if self.units == "celsius":
            weather["temp"] = self.temp - 273.15
            return weather
        if self.units == "kelvin":
            weather["temp"] = self.temp
            return weather


class UserAuth:
    def __init__(self, email, password):
        self.email = email
        self.password = password
