from Extract.openweather import fetch_openweather
from Extract.openmeteo import fetch_openmeteo
from Extract.weatherapi import fetch_weatherapi
from pathlib import Path
import json

SCHEMA_DIR = Path(__file__).parent / "data_schemas"
SCHEMA_DIR.mkdir(exist_ok=True)

def flatten(payload, label="payload"):
    current = {}

    if isinstance(payload, dict):
        for k, v in payload.items():
            separator = ":" if label == "payload" else "."
            current.update(flatten(v, f"{label}{separator}{k}"))

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
        s.append(f"    {k}::{v} as {k.replace('payload', '').replace(':', '_').replace('[0]', '').replace('_', '').replace('.', '_')}")

    print("select")
    print(", \n".join(s))
    print(f"from {db}.{table};")

def save_schema(schema, source):
    schema_file = SCHEMA_DIR / f"{source}_schema.json"
    with open(schema_file, "w") as f:
        json.dump(schema, f, indent=4)

def compare_schema(new_schema, source):
    added = {}
    removed = {}
    changed = {}

    schema_file = SCHEMA_DIR / f"{source}_schema.json"
    with open(schema_file, "r") as f:
        old_schema = json.load(f)

    for k, v in new_schema.items():
        if k not in old_schema:
            added[k] = v
        elif old_schema[k] != v:
            changed[k] = (old_schema[k], v)

    for k, v in old_schema.items():
        if k not in new_schema:
            removed[k] = v

    if added:
        print("New fields detected:")
        for k, v in added.items():
            print(f"  + {k} ({v})")

    if removed:
        print("Removed fields:")
        for k, v in removed.items():
            print(f"  - {k} ({v})")

    if changed:
        print("Type changes:")
        for k, (old_t, new_t) in changed.items():
            print(f"  * {k}: {old_t} -> {new_t}")

    if not (added or removed or changed):
        print("No schema drift detected.")

sample1 = fetch_openweather("Manila")
sample2 = fetch_openmeteo({"lat": 14.5995, "lon": 120.9842})
sample3 = fetch_weatherapi("Manila")

schema1 = flatten(sample1)
schema2 = flatten(sample2)
schema3 = flatten(sample3)

compare_schema(schema1, "openweather")

# python -m tools.generate_snowflake_staging