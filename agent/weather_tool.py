import requests

def get_current_weather(location: str):
    """
    Gets the current weather for a given location using Open-Meteo.

    Args:
        location: The name of the city, e.g. "London", "New York".
    """
    # 1. Geocoding: Get lat/lon for the location
    geocoding_url = "https://geocoding-api.open-meteo.com/v1/search"
    geo_params = {
        "name": location,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    try:
        geo_response = requests.get(geocoding_url, params=geo_params)
        geo_response.raise_for_status()
        geo_data = geo_response.json()

        if not geo_data.get("results"):
            return f"Error: City '{location}' not found."

        lat = geo_data["results"][0]["latitude"]
        lon = geo_data["results"][0]["longitude"]
        city_name = geo_data["results"][0]["name"]

        # 2. Weather: Get current weather using lat/lon
        weather_url = "https://api.open-meteo.com/v1/forecast"
        weather_params = {
            "latitude": lat,
            "longitude": lon,
            "current": ["temperature_2m", "weather_code"],
            "timezone": "auto"
        }

        weather_response = requests.get(weather_url, params=weather_params)
        weather_response.raise_for_status()
        weather_data = weather_response.json()

        current = weather_data.get("current", {})
        temp = current.get("temperature_2m")
        weather_code = current.get("weather_code")
        
        # Simple WMO weather code interpretation
        # https://open-meteo.com/en/docs
        description = "Unknown"
        if weather_code == 0: description = "Clear sky"
        elif weather_code in [1, 2, 3]: description = "Mainly clear, partly cloudy, and overcast"
        elif weather_code in [45, 48]: description = "Fog"
        elif weather_code in [51, 53, 55]: description = "Drizzle"
        elif weather_code in [61, 63, 65]: description = "Rain"
        elif weather_code in [71, 73, 75]: description = "Snow fall"
        elif weather_code in [95, 96, 99]: description = "Thunderstorm"

        return f"The weather in {city_name} is {description} with a temperature of {temp}°C."

    except requests.exceptions.RequestException as e:
        return f"Error fetching weather data: {e}"
    except KeyError:
        return "Error parsing weather data."
