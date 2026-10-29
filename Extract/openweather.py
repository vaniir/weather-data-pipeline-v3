import requests
from config.settings import OPENWEATHER_KEY

openweather_url = "https://api.openweathermap.org/data/2.5/weather"

def fetch_openweather(city: str):

    openweather_param = {
        "q": f"{city},PH",
        "units": "metric",
        "APPID": OPENWEATHER_KEY
    }

    openweather_response = requests.get(openweather_url, params=openweather_param, timeout=(5, 30))
    openweather_response.raise_for_status()

    return openweather_response.json()