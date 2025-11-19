from weather_tool import get_current_weather

print("Testing London:")
print(get_current_weather("London"))

print("\nTesting New York:")
print(get_current_weather("New York"))

print("\nTesting Invalid City:")
print(get_current_weather("InvalidCityName12345"))
