from weather_forecast_system.facade.weather_api_facade import WeatherAPIFacade

class WeatherDataCacheProxy:
    def __init__(self):
        self.weather_api_facade = WeatherAPIFacade()
        self.cache = {}

    def get_weather_data(self, location):
        if location not in self.cache:
            self.cache[location] = self.weather_api_facade.get_weather_data(location)
        return self.cache[location]
