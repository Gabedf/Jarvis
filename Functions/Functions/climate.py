import requests as r
import json 

# API CLIMA
def climate():
    url = "https://api.weatherbit.io/v2.0/current"
    state = input("Insira o estado: ")
    city = input("Insira a cidade: ")
    params = {
        'state': state,
        'city': city,
        'country': 'BR',
        'key': '1e1d3c676ef74107b52a21f2ebfd67d9'
    }
    response = r.get(url, params=params)
    data = response.json()

    return data['data'][0]['temp']
    