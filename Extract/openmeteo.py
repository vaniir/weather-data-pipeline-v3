import requests

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

def fetch_openmeteo(coordinates):
    lat = coordinates["lat"]
    lon = coordinates["lon"]

    openmeteo_param = {
        "latitude": lat,
        "longitude": lon,
        "current": openmeteo_current
    }

    openmeteo_response = requests.get(openmeteo_url, params=openmeteo_param)

    return openmeteo_response.json()
