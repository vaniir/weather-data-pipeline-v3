from Extract.openweather import fetch_openweather
from Extract.openmeteo import fetch_openmeteo
from Extract.weatherapi import fetch_weatherapi

def flatten(payload, label="payload"):
    x = []

    if isinstance(payload, dict):
        for k, v in payload.items():
            x.extend(flatten(v, f"{label}:{k}"))

    elif isinstance(payload, list):
        if payload:
            x.extend(flatten(payload[0], f"{label}[0]"))

    else:
        if isinstance(payload, bool):
            dt = "BOOLEAN"
        elif isinstance(payload, int):
            dt = "INTEGER"
        elif isinstance(payload, float):
            dt = "FLOAT"
        else:
            dt = "STRING"

        name = label.replace("payload", "").replace(":", "_").replace(".", "_")
        x.append(f"     {label}::{dt.lower()} as {name}")

    return x


sample = fetch_weatherapi("Manila")

print("select")
print(", \n".join(flatten(sample)))
print("from weather_data.raw.weatherapi_raw;")
