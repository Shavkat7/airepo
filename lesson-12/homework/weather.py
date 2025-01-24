import requests

API_key = '10f4eba66c1fe3914d9fb4fd5ae9d7c2'

city_name = input('Enter city name: ')

lat_lon = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={API_key}"
response = requests.get(lat_lon)
lon = response.json()[0]['lon']
lat = response.json()[0]['lat']

url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}'

print(requests.get(url).json()['main'])