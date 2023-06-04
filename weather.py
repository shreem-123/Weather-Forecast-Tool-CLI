import requests
import json
import sys

def get_weather(city):
    api_key = "bc315051c7628fcaac83c4fbdeb5d5f2"  
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        weather_data = response.json()

        # Parse the weather data
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']

        # Display the weather forecast
        print(f"Weather forecast for {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Description: {description}")

    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        sys.exit(1)
    except (KeyError, IndexError, json.JSONDecodeError):
        print("Failed to parse weather data.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a city name as an argument.")
        sys.exit(1)

    city_name = " ".join(sys.argv[1:])
    get_weather(city_name)
