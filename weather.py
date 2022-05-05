
import requests
import json
KEY = '48540db1cd65c8fee473a770b843e073'

def weather_get(lat,lon):
    API_URL_json = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={KEY}'
    response = requests.get(API_URL_json)
    data=json.loads(response.text)
    return data