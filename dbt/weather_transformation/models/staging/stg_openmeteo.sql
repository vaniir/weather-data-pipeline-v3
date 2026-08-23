select
    -- Location metadata
    payload:latitude::FLOAT as latitude,
    payload:longitude::FLOAT as longitude,
    payload:elevation::FLOAT as elevation,
    payload:timezone::STRING as timezone,
    payload:timezone_abbreviation::STRING as timezone_abbreviation,
    payload:utc_offset_seconds::INTEGER as utc_offset_seconds,

    -- API metadata
    payload:generationtime_ms::FLOAT as generation_time_ms,
    DATEADD(
        SECOND,
        -payload:utc_offset_seconds::INTEGER,
        TO_TIMESTAMP_NTZ(payload:current.time::STRING)
    ) AS observation_timestamp,

    -- Current weather units
    payload:current_units.time::STRING as time_unit,
    payload:current_units.interval::STRING as interval_unit,
    payload:current_units.temperature_2m::STRING as temperature_unit,
    payload:current_units.apparent_temperature::STRING as apparent_temperature_unit,
    payload:current_units.relative_humidity_2m::STRING as humidity_unit,
    payload:current_units.pressure_msl::STRING as pressure_unit,
    payload:current_units.wind_speed_10m::STRING as wind_speed_unit,
    payload:current_units.wind_direction_10m::STRING as wind_direction_unit,
    payload:current_units.cloud_cover::STRING as cloud_cover_unit,
    payload:current_units.precipitation::STRING as precipitation_unit,
    payload:current_units.weather_code::STRING as weather_code_unit,
    payload:current_units.is_day::STRING as is_day_unit,

    -- Current weather
    payload:current.time::STRING as time,
    payload:current.interval::INTEGER as interval,
    payload:current.temperature_2m::FLOAT as temperature,
    payload:current.apparent_temperature::FLOAT as apparent_temperature,
    payload:current.relative_humidity_2m::INTEGER as humidity,
    payload:current.pressure_msl::FLOAT as pressure,
    payload:current.wind_speed_10m::FLOAT as wind_speed,
    payload:current.wind_direction_10m::INTEGER as wind_direction,
    payload:current.cloud_cover::INTEGER as cloud_cover,
    payload:current.precipitation::FLOAT as precipitation,
    payload:current.weather_code::INTEGER as weather_code,
    payload:current.is_day::INTEGER as is_day

from weather_data.raw.openmeteo_raw