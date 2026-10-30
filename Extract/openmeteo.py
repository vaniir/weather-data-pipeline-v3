
import requests
import time

openmeteo_url = "https://api.open-meteo.com/v1/forecast"

openmeteo_current = ",".join([
    "temperature_2m",
    "apparent_temperature",
    "relative_humidity_2m",
    "pressure_msl",
    "wind_speed_10m",
    "wind_direction_10m",
    "cloud_cover",
    "precipitation",
    "weather_code",
    "is_day"
])

def fetch_openmeteo(coordinates: dict):
    lat = coordinates["lat"]
    lon = coordinates["lon"]

    openmeteo_param = {
        "latitude": lat,
        "longitude": lon,
        "current": openmeteo_current
    }

    start = time.monotonic()

    try:
        openmeteo_response = requests.get(
            openmeteo_url,
            params=openmeteo_param,
            timeout=(5, 30)
        )

    except requests.exceptions.Timeout as e:
        elapsed = time.monotonic() - start

        print(f"[Open-Meteo] FAILED | {lat}, {lon}")
        print(f"Elapsed: {elapsed:.2f} seconds")
        print(f"Exception: {e!r}")
        raise

    elapsed = time.monotonic() - start
    print(f"[Open-Meteo] SUCCESS | {lat}, {lon} | {elapsed:.2f} seconds")

    openmeteo_response.raise_for_status()

    return openmeteo_response.json()
