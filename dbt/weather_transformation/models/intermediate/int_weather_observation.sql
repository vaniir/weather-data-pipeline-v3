select
    ow.name as city_name,
    ow.coord_lat as latitude,
    ow.coord_lon as longitude,

    ow.observation_timestamp as observation_timestamp,

    ow.temp as temp,
    ow.humidity as humidity,
    ow.feels_like as feels_like,
    ow.pressure as pressure,
    ow.wind_speed as wind_speed,

    ow.weather_description as weather_description

from {{ ref('stg_openweather') }} as ow

union all

select
    wa.location_name as city_name,
    wa.location_lat as latitude,
    wa.location_lon as longitude,

    wa.observation_timestamp as observation_timestamp,

    wa.temp_c as temp,
    wa.humidity as humidity,
    wa.feels_like_c as feels_like,
    wa.pressure_mb as pressure,
    wa.wind_speed_kph as wind_speed,

    wa.weather_condition_text as weather_description

from {{ ref('stg_weatherapi') }} as wa
    
union all

select
    NULL::STRING as city_name, -- will neeed to map city name from lat/lon using reverse geocoding
    om.latitude as latitude,
    om.longitude as longitude,

    om.observation_timestamp as observation_timestamp,

    om.temperature as temp,
    om.humidity as humidity,
    om.apparent_temperature as feels_like,
    om.pressure as pressure,
    om.wind_speed as wind_speed,

    w.weather_description as weather_description

from {{ ref('stg_openmeteo') }} as om
    
left join {{ ref('weather_code_mapping') }} as w
    on om.weather_code = w.weather_code 
    and w.source = 'openmeteo'
