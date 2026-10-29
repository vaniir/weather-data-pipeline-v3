from config.cities import CITIES
from Extract.openweather import fetch_openweather
from Extract.openmeteo import fetch_openmeteo
from Extract.weatherapi import fetch_weatherapi
from Load.snowflake_loader import load_to_snowflake

def run():
    failed_requests = [] # for github action
    successful_requests = [] # for github action

    for city, coords in CITIES.items():
        latitude = coords["lat"]
        longitude = coords["lon"]
        try:
            payload = fetch_openweather(city)
            load_to_snowflake("OPENWEATHER_RAW", city, latitude, longitude, payload)
            successful_requests.append(("OpenWeather", city))
        except Exception as e:
            failed_requests.append(("OpenWeather", city, str(e)))
            print(f"OpenWeather failed for {city}")
            print(f"Error type: {type(e)}")
            print(f"Error: {repr(e)}")
        try:
            payload = fetch_openmeteo(coords)
            load_to_snowflake("OPENMETEO_RAW", city, latitude, longitude, payload)
            successful_requests.append(("OpenMeteo", city))
        except Exception as e:
            failed_requests.append(("OpenMeteo", city, str(e)))
            print(f"OpenMeteo failed for {city}")
            print(f"Error type: {type(e)}")
            print(f"Error: {repr(e)}")

        try:
            payload = fetch_weatherapi(city)
            load_to_snowflake("WEATHERAPI_RAW", city, latitude, longitude, payload)
            successful_requests.append(("WeatherAPI", city))
        except Exception as e:
            failed_requests.append(("WeatherAPI", city, str(e)))
            print(f"WeatherAPI failed for {city}")
            print(f"Error type: {type(e)}")
            print(f"Error: {repr(e)}")

    if failed_requests:
        print("\n=== FAILED INGESTION ATTEMPTS ===")

        for source, city, error in failed_requests:
            print(f"{source} | {city} | {error}")

        raise RuntimeError(
            f"Ingestion finished with {len(failed_requests)} failed ingestion attempt(s)."
        )

    for source, city in successful_requests:
        print(f"{source} | {city} | Ingestion successful.")

if __name__ == "__main__":
    run()

