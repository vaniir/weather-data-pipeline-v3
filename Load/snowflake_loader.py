from config import settings
import snowflake.connector
import json

payload = {
    "hellow" : "world",
    "test": "succeed"
}

conn = snowflake.connector.connect(
    user=settings.SNOWFLAKE_USER,
    password=settings.SNOWFLAKE_PASSWORD,
    account=settings.SNOWFLAKE_ACCOUNT,
    warehouse=settings.SNOWFLAKE_WAREHOUSE,
    database=settings.SNOWFLAKE_DATABASE,
    schema=settings.SNOWFLAKE_SCHEMA
)

cursor = conn.cursor()

cursor.execute("""
    INSERT INTO OPENWEATHER_RAW (payload)
    SELECT PARSE_JSON(%s)
""",(json.dumps(payload),)
)
conn.commit()

cursor.close()
conn.close()