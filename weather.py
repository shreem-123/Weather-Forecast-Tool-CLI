# import requests
# import json
# import sys

# def get_weather(city):
#     api_key = "bc315051c7628fcaac83c4fbdeb5d5f2"  
#     base_url = "http://api.openweathermap.org/data/2.5/weather"

#     params = {
#         "q": city,
#         "appid": api_key,
#         "units": "metric"
#     }

#     try:
#         response = requests.get(base_url, params=params)
#         response.raise_for_status()
#         weather_data = response.json()

#         # Parse the weather data
#         temperature = weather_data['main']['temp']
#         description = weather_data['weather'][0]['description']

#         # Display the weather forecast
#         print(f"Weather forecast for {city}:")
#         print(f"Temperature: {temperature}°C")
#         print(f"Description: {description}")

#     except requests.exceptions.RequestException as e:
#         print(f"Error occurred: {e}")
#         sys.exit(1)
#     except (KeyError, IndexError, json.JSONDecodeError):
#         print("Failed to parse weather data.")
#         sys.exit(1)

# if __name__ == "__main__":
#     if len(sys.argv) < 2:
#         print("Please provide a city name as an argument.")
#         sys.exit(1)

#     city_name = " ".join(sys.argv[1:])
#     get_weather(city_name)
import requests

def get_weather(city):
    api_key = "bc315051c7628fcaac83c4fbdeb5****"
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    try:
        params = {
            "q": city,
            "appid": api_key,
            "units": "metric"
        }

        response = requests.get(base_url, params=params)
        response.raise_for_status()

        weather_data = response.json()

        # Extract relevant weather information from the response
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]

        # Display the weather forecast to the user
        print(f"Weather forecast for {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")

    except requests.exceptions.RequestException as e:
        print("Error occurred during API request:", e)
    except KeyError as e:
        print("Error occurred during data parsing:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)

city = "London"
get_weather(city)
