import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather(city: str):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "APPID": API_KEY, "units": "metric"}
    try:
        resp = requests.get(url, params=params, timeout=5)
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.HTTPError as e:
        print(f"API error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
    return None

if __name__ == "__main__":
    print("Hello World.", "API_KEY: ", API_KEY)
    result = get_weather("Lagos")
    if result:
        print(f"{result['name']}: {result['main']['temp']}°C")