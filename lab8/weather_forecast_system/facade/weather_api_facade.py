from ..weather_api.weather_api import WeatherAPI1, WeatherAPI2

class WeatherAPIFacade:
    def __init__(self):
        self.weather_api1 = WeatherAPI1()
        self.weather_api2 = WeatherAPI2()

    def get_weather_data(self, location):
        weather_data = self.weather_api1.get_weather(location)

        if weather_data is None:
            weather_data = self.weather_api2.get_weather(location)

        return weather_data
