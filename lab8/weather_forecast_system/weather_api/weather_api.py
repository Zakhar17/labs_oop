import random

class WeatherAPI1:
    def get_weather(self, location):
        # Simulate an API request by returning random weather data or None
        return {
            "location": location,
            "temperature": random.randint(-10, 35),
            "humidity": random.randint(0, 100),
        } if random.random() > 0.1 else None

class WeatherAPI2:
    def get_weather(self, location):
        # Simulate an API request by returning random weather data or None
        return {
            "location": location,
            "temperature": random.randint(-10, 35),
            "humidity": random.randint(0, 100),
        } if random.random() > 0.1 else None
