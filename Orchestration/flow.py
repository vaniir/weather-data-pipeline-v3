from config.cities import CITIES
from Extract.openweather import fetch_openweather
from Extract.openmeteo import fetch_openmeteo
from Extract.weatherapi import fetch_weatherapi
from Load.snowflake_loader import load_to_snowflake

def run():
    for city, coords in CITIES.items():
        latitude = coords["lat"]
        longitude = coords["lon"]
        try:
            payload = fetch_openweather(city)
            load_to_snowflake("OPENWEATHER_RAW", city, latitude, longitude, payload)
        except Exception as e:
            print(f"OpenWeather failed for {city}")
            print(f"Error type: {type(e)}")
            print(f"Error: {repr(e)}")
        try:
            payload = fetch_openmeteo(coords)
            load_to_snowflake("OPENMETEO_RAW", city, latitude, longitude, payload)
        except Exception as e:
            print(f"OpenMeteo failed for {city}")
            print(f"Error type: {type(e)}")
            print(f"Error: {repr(e)}")

        try:
            payload = fetch_weatherapi(city)
            load_to_snowflake("WEATHERAPI_RAW", city, latitude, longitude, payload)
        except Exception as e:
            print(f"WeatherAPI failed for {city}")
            print(f"Error type: {type(e)}")
            print(f"Error: {repr(e)}")

if __name__ == "__main__":
    run()

