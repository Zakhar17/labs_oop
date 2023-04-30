from weather_forecast_system.proxy.weather_data_cache_proxy import WeatherDataCacheProxy
from weather_forecast_system.bridge.data_format_bridge import JSONFormat, XMLFormat

def main():
    location = "New York"
    weather_data_cache_proxy = WeatherDataCacheProxy()

    weather_data = weather_data_cache_proxy.get_weather_data(location)

    if weather_data is None:
        print(f"No weather data found for {location}.")
    else:
        json_format = JSONFormat()
        xml_format = XMLFormat()

        json_formatted_data = json_format.format_data(weather_data)
        xml_formatted_data = xml_format.format_data(weather_data)

        print(f"Weather data for {location} in JSON format:\n{json_formatted_data}\n")
        print(f"Weather data for {location} in XML format:\n{xml_formatted_data}")

if __name__ == "__main__":
    main()



# def main():
#     weather_data_proxy = WeatherDataCacheProxy()
#     json_format_bridge = JSONFormat()
#     xml_format_bridge = XMLFormat()
#
#     location = "New York"
#     weather_data = weather_data_proxy.get_weather_data(location)
#
#     json_formatted_data = json_format_bridge.format_data(weather_data)
#     xml_formatted_data = xml_format_bridge.format_data(weather_data)
#
#     print(f"Weather data for {location} in JSON format:\n{json_formatted_data}")
#     print(f"Weather data for {location} in XML format:\n{xml_formatted_data}")
#
#
# if __name__ == "__main__":
#     main()
