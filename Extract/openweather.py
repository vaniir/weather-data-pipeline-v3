import requests
from config.settings import OPENWEATHER_KEY

openweather_url = "https://api.openweathermap.org/data/2.5/weather"

def fetch_openweather(city: str):

    openweather_param = {
        "q": f"{city},PH",
        "units": "metric",
        "APPID": OPENWEATHER_KEY
    }

    openweather_response = requests.get(openweather_url, params=openweather_param)

    return openweather_response.json()