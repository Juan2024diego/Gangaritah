class CityWeather:


    def __init__(self, name, weather, temp, humidity, wind_speed, type_degrees):
        self.name = name
        self.weather = weather
        self.temp = temp
        self.humidity = humidity
        self.wind_speed = wind_speed
        self.type_degrees = type_degrees
    

    def to_json(self):
        weather = {
                "name": self.name,
                "weather": self.weather,
                "humidity": self.humidity,
                "wind_speed": self.wind_speed
            }
        if self.type_degrees == "celsius":
            weather["temp"] = self.temp - 273.15
            return weather
        if self.type_degrees == "kelvin":
            weather["temp"] = self.temp
            return weather

