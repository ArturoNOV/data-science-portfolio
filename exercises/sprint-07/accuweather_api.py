import os
import pprint
import requests


api_key = os.getenv('ACCUWEATHER_API_KEY')

if not api_key:
    raise SystemExit(
        'No se encontró la variable de entorno ACCUWEATHER_API_KEY. '
        'Configura tu API key antes de ejecutar el programa.'
    )

params = {'apikey': api_key, 'q': 'New York'}

aw_location_url = (
    "https://dataservice.accuweather.com/locations/v1/cities/search"
)
aw_location_res = requests.get(aw_location_url, params=params)
aw_location_res.raise_for_status()

pprint.pprint(aw_location_res.json())

print()

for loc_info in aw_location_res.json():
    print(
        '{:>8}   {:10}   {:16}    {:16}'.format(
            loc_info['Key'],
            loc_info['EnglishName'],
            loc_info['Country']['EnglishName'],
            loc_info['AdministrativeArea']['EnglishName'],
        )
    )

print()

params = {'apikey': api_key, 'metric': True}

location_id = 349727
aw_forecast_url = (
    'https://dataservice.accuweather.com/forecasts/v1/daily/5day/'
    + str(location_id)
)

aw_forecast_res = requests.get(aw_forecast_url, params=params)
aw_forecast_res.raise_for_status()

for daily_forecast in aw_forecast_res.json()['DailyForecasts']:
    print(
        '{}   {:30} {}{}  {}{}'.format(
            daily_forecast['Date'],
            daily_forecast['Day']['IconPhrase'],
            daily_forecast['Temperature']['Minimum']['Value'],
            daily_forecast['Temperature']['Minimum']['Unit'],
            daily_forecast['Temperature']['Maximum']['Value'],
            daily_forecast['Temperature']['Maximum']['Unit'],
        )
    )
