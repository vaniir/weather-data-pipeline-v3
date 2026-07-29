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

def load_to_snowflake(table_name: str, payload: dict):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(f"""
        INSERT INTO {table_name} (payload)
        SELECT PARSE_JSON(%s)
    """,(json.dumps(payload),)
    )

    conn.commit()
    cursor.close()
    conn.close()