-- average temperature, humidity, and feels_like for each source per city per day

select

    cast(
        convert_timezone('UTC', 'Asia/Manila', observation_timestamp)
        as date
    ) as observation_date,

    city_name,
    source,

    round(avg(temp), 2) as avg_temp,
    round(avg(humidity), 2) as avg_humidity,
    round(avg(feels_like), 2) as avg_feels_like

from {{ ref('int_weather_observation') }}

group by 

    source, 
    city_name, 
    cast(
        convert_timezone('UTC', 'Asia/Manila', observation_timestamp)
        as date
    )
