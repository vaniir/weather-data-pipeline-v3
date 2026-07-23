import requests
from config.settings import WEATHERAPI_KEY
import json

weatherapi_url = "http://api.weatherapi.com/v1/current.json"

def fetch_weatherapi(city):

    weatherapi_param = {
        "key": WEATHERAPI_KEY,
        "q": f"{city},PH"
    }

    weatherapi_response = requests.get(weatherapi_url, params=weatherapi_param)

    return weatherapi_response.json()