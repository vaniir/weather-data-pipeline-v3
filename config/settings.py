from dotenv import load_dotenv
import os

load_dotenv()

OPENWEATHER_KEY = os.getenv("openweather_key")
WEATHERAPI_KEY = os.getenv("weatherapi_key")