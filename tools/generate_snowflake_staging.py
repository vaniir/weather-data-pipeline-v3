from Extract.openweather import fetch_openweather
from Extract.openmeteo import fetch_openmeteo
from Extract.weatherapi import fetch_weatherapi

def flatten(payload, label="payload"):
    current = {}

    if isinstance(payload, dict):
        for k, v in payload.items():
            current.update(flatten(v, f"{label}:{k}"))

    elif isinstance(payload, list):
        if payload:
            current.update(flatten(payload[0], f"{label}[0]"))

    else:
        if isinstance(payload, bool):
            dt = "BOOLEAN"
        elif isinstance(payload, int):
            dt = "INTEGER"
        elif isinstance(payload, float):
            dt = "FLOAT"
        else:
            dt = "STRING"

        current[label] = dt

    return current

def create_schema(flattened, db="weather_data", table="raw.weatherapi_raw"):
    s = []
    for k, v in flattened.items():
        s.append(f"    {k}::{v} as {k.replace('payload', '').replace(':', '_').replace('[0]', '')}")

    print("select")
    print(", \n".join(s))
    print(f"from {db}.{table};")

# add save_schema and compare_schema functions

sample = fetch_weatherapi("Manila")
flattened = flatten(sample)
create_schema(flattened)

# print("select")
# print(", \n".join(flatten(sample)))
# print("from weather_data.raw.weatherapi_raw;")
