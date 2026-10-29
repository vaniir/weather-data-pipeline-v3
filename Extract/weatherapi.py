import requests
from config.settings import WEATHERAPI_KEY
import json

weatherapi_url = "http://api.weatherapi.com/v1/current.json"

def fetch_weatherapi(city: str):

    weatherapi_param = {
        "key": WEATHERAPI_KEY,
        "q": f"{city},PH"
    }

    weatherapi_response = requests.get(weatherapi_url, params=weatherapi_param, timeout=(10, 30))
    weatherapi_response.raise_for_status() 

    return weatherapi_response.json()