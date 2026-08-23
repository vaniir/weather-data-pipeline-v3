select
    -- Location
    payload:name::STRING as name,
    payload:id::INTEGER as id,
    payload:coord.lon::FLOAT as coord_lon,
    payload:coord.lat::FLOAT as coord_lat,
    payload:timezone::INTEGER as timezone,

    -- API metadata
    payload:base::STRING as base,
    to_timestamp_ntz(payload:dt::INTEGER) as observation_timestamp,
    payload:cod::INTEGER as response_code,

    -- Weather condition
    payload:weather[0].id::INTEGER as weather_id,
    payload:weather[0].main::STRING as weather_main,
    payload:weather[0].description::STRING as weather_description,
    payload:weather[0].icon::STRING as weather_icon,

    -- Atmospheric measurements
    payload:main.temp::FLOAT as temp,
    payload:main.feels_like::FLOAT as feels_like,
    payload:main.temp_min::FLOAT as temp_min,
    payload:main.temp_max::FLOAT as temp_max,
    payload:main.pressure::INTEGER as pressure,
    payload:main.humidity::INTEGER as humidity,
    payload:main.sea_level::INTEGER as sea_level,
    payload:main.grnd_level::INTEGER as ground_level,
    payload:visibility::INTEGER as visibility,

    -- Wind
    payload:wind.speed::FLOAT as wind_speed,
    payload:wind.deg::INTEGER as wind_direction,
    payload:wind.gust::FLOAT as wind_gust,

    -- Precipitation and clouds
    payload:rain['1h']::FLOAT as rain,
    payload:clouds.all::INTEGER as cloud_cover,

    -- System information
    payload:sys.country::STRING as country,
    payload:sys.sunrise::INTEGER as sunrise,
    payload:sys.sunset::INTEGER as sunset

from weather_data.raw.openweather_raw