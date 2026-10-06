from config import settings
import snowflake.connector
import json

def get_connection():
    return snowflake.connector.connect(
        user=settings.SNOWFLAKE_USER,
        password=settings.SNOWFLAKE_PASSWORD,
        account=settings.SNOWFLAKE_ACCOUNT,
        warehouse=settings.SNOWFLAKE_WAREHOUSE,
        database=settings.SNOWFLAKE_DATABASE,
        schema=settings.SNOWFLAKE_SCHEMA
    )

def load_to_snowflake(table_name: str, city_name: str, latitude: float, longitude: float, payload: dict):
    conn = get_connection()
    cursor = conn.cursor()

    observation_key = ""
    if table_name.lower().replace("_raw", "") == "openweather":
        observation_key = "payload:dt::INTEGER"
    elif table_name.lower().replace("_raw", "") == "weatherapi":
        observation_key = "payload:current.last_updated::STRING"
    elif table_name.lower().replace("_raw", "") == "openmeteo":
        observation_key = "payload:current.time::STRING"

    cursor.execute(f"""

        MERGE INTO WEATHER_DATA.RAW.{table_name} AS target
        USING (
            SELECT
                %s AS city_name,
                %s AS latitude,
                %s AS longitude,
                PARSE_JSON(%s) AS payload
        ) AS incoming

        ON target.city_name = incoming.city_name
        AND {observation_key.replace('payload:', 'target.payload:')} = {observation_key.replace('payload:', 'incoming.payload:')}

        WHEN NOT MATCHED THEN
        INSERT (city_name, latitude, longitude, payload)
        VALUES (
            incoming.city_name,
            incoming.latitude,
            incoming.longitude,
            incoming.payload
            )
    """,
        (
            city_name,
            latitude,
            longitude,
            json.dumps(payload)
        )
    )

    conn.commit()
    cursor.close()
    conn.close()