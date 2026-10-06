select
    'openweather' as source,

    ow.city_name as city_name,
    ow.latitude as latitude,
    ow.longitude as longitude,

    ow.observation_timestamp as observation_timestamp,

    ow.temperature as temp,
    ow.humidity as humidity,
    ow.feels_like as feels_like,
    ow.pressure as pressure,
    round(ow.wind_speed * 3.6, 2) as wind_speed, -- from m/s to km/h
    ow.wind_direction as wind_direction,

    ow.weather_description as weather_description

from {{ ref('stg_openweather') }} as ow

union all

select
    'weatherapi' as source,

    wa.city_name as city_name,
    wa.latitude as latitude,
    wa.longitude as longitude,

    wa.observation_timestamp as observation_timestamp,

    wa.temperature as temp,
    wa.humidity as humidity,
    wa.feels_like as feels_like,
    wa.pressure as pressure,
    wa.wind_speed as wind_speed,
    wd.direction_degrees as wind_direction,

    wa.weather_description as weather_description

from {{ ref('stg_weatherapi') }} as wa

left join {{ ref('weather_direction_mapping') }} as wd
    on wa.wind_direction = wd.wind_direction
    
union all

select
    'openmeteo' as source,

    om.city_name as city_name, -- from metadata
    om.latitude as latitude,
    om.longitude as longitude,

    om.observation_timestamp as observation_timestamp,

    om.temperature as temp,
    om.humidity as humidity,
    om.feels_like as feels_like,
    om.pressure as pressure,
    om.wind_speed as wind_speed,
    om.wind_direction as wind_direction,

    wc.weather_description as weather_description

from {{ ref('stg_openmeteo') }} as om
    
left join {{ ref('weather_code_mapping') }} as wc
    on om.weather_code = wc.weather_code 
    and wc.source = 'openmeteo'
