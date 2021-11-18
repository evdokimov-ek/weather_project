import requests


OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall?"
API_KEY = "8bbb0231728b848fd66447fcafb0ee1d"

weather_params = {
    "lat": 55.745147,
    "lon": 37.797432,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data['hourly'][:12]

will_rain = False
for hour in weather_slice:
    condition_code = hour['weather'][0]['id']
    print(condition_code)
    if int(condition_code)<600:
        will_rain = True
if will_rain:
    print('Bring an umbrella')
else:
    print("You don't need an umbrella")
