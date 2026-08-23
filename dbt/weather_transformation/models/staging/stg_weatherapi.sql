select
    -- Location
    payload:location.name::STRING as location_name,
    payload:location.region::STRING as location_region,
    payload:location.country::STRING as location_country,
    payload:location.lat::FLOAT as location_lat,
    payload:location.lon::FLOAT as location_lon,
    payload:location.tz_id::STRING as location_tz_id,
    payload:location.localtime_epoch::INTEGER as location_localtime_epoch,
    payload:location.localtime::STRING as location_localtime,

    -- API metadata
    payload:current.last_updated_epoch::INTEGER as timestamp,
    payload:current.last_updated::STRING as last_updated,
    CONVERT_TIMEZONE(
        payload:location.tz_id::STRING,
        'UTC',
        TO_TIMESTAMP_NTZ(payload:current.last_updated::STRING)
    )::TIMESTAMP_NTZ AS observation_timestamp,

    -- Weather condition
    payload:current.is_day::INTEGER as is_day,
    payload:current.condition.text::STRING as weather_condition_text,
    payload:current.condition.icon::STRING as weather_condition_icon,
    payload:current.condition.code::INTEGER as weather_condition_code,

    -- Atmospheric measurements
    payload:current.temp_c::FLOAT as temp_c,
    payload:current.temp_f::FLOAT as temp_f,
    payload:current.feelslike_c::FLOAT as feels_like_c,
    payload:current.feelslike_f::FLOAT as feels_like_f,
    payload:current.pressure_mb::FLOAT as pressure_mb,
    payload:current.pressure_in::FLOAT as pressure_in,
    payload:current.humidity::INTEGER as humidity,
    payload:current.cloud::INTEGER as cloud_cover,

    -- Wind
    payload:current.wind_kph::FLOAT as wind_speed_kph,
    payload:current.wind_mph::FLOAT as wind_speed_mph,
    payload:current.wind_degree::INTEGER as wind_direction_deg,
    payload:current.wind_dir::STRING as wind_direction,
    payload:current.gust_kph::FLOAT as wind_gust_kph,
    payload:current.gust_mph::FLOAT as wind_gust_mph,

    -- Precipitation
    payload:current.precip_mm::FLOAT as precipitation_mm,
    payload:current.precip_in::FLOAT as precipitation_in,
    payload:current.will_it_rain::INTEGER as will_rain,
    payload:current.chance_of_rain::INTEGER as chance_of_rain,
    payload:current.will_it_snow::INTEGER as will_snow,
    payload:current.chance_of_snow::INTEGER as chance_of_snow,

    -- Visibility and UV
    payload:current.vis_km::FLOAT as visibility_km,
    payload:current.vis_miles::FLOAT as visibility_miles,
    payload:current.uv::FLOAT as uv_index,

    -- Derived measurements
    payload:current.windchill_c::FLOAT as wind_chill_c,
    payload:current.windchill_f::FLOAT as wind_chill_f,
    payload:current.heatindex_c::FLOAT as heat_index_c,
    payload:current.heatindex_f::FLOAT as heat_index_f,
    payload:current.dewpoint_c::FLOAT as dew_point_c,
    payload:current.dewpoint_f::FLOAT as dew_point_f,
    payload:current.wetbulb_c::FLOAT as wet_bulb_c,
    payload:current.wetbulb_f::FLOAT as wet_bulb_f

from weather_data.raw.weatherapi_raw