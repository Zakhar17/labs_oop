# Weather Forecast System

The Weather Forecast System retrieves weather data from multiple weather APIs using the Facade pattern, caches the data using the Proxy pattern, and can switch between different data formats using the Bridge pattern.

## Requirements

1. Implement a WeatherAPIFacade class that interacts with multiple weather API services.
2. Implement a WeatherDataCacheProxy class that caches weather data and delegates requests to the WeatherAPIFacade.
3. Implement a DataFormatBridge class that allows switching between
different data formats (e.g., JSON, XML) when displaying the weather data.
4. Create a clear and organized project directory structure with separate folders for Facade, Proxy, Bridge, and WeatherAPI classes.

## Usage
1. Instantiate a WeatherDataCacheProxy object.
2. Instantiate a DataFormatBridge object with the desired data format (JSONFormat or XMLFormat).
3. Retrieve weather data for a specific location using the get_weather_data method of the WeatherDataCacheProxy object.
4. Display the weather data in the chosen format using the format_data method of the DataFormatBridge object.
