import pprint
from urllib.request import urlopen
from urllib.parse import urlencode, quote_plus
import json

API_KEY = "41028f4e1a2818b4b681d5527b7c258b"
geo_url = f"http://api.openweathermap.org/geo/1.0/direct"
params = {
    'appid': API_KEY,
}
city = input("insert city: ")
params['q'] = city
# Encode spaces with '+' (preferred in URLs)
query_string = urlencode(params, quote_via=quote_plus)
geo_url = geo_url + f"?{query_string}"

print(f"geo_url: {geo_url}")
geo_response = urlopen(geo_url)

# print(geo_url)

geo_data = json.loads(geo_response.read())
# pprint.pprint(json.loads(geo_response.read()))

lat = geo_data[0]['lat']
long = geo_data[0]['lon']

weather_url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "appid": API_KEY,
    "lat": lat,
    "lon": long,
    "units": "metric"
}
query_string = urlencode(params, quote_via=quote_plus)
weather_url = weather_url + f"?{query_string}"

print(f"weather_url: {weather_url}")
weather_response = urlopen(weather_url)

pprint.pprint(json.loads(weather_response.read()))


