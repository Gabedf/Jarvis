import requests as r
import json 

prices = r.get(" https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
prices = prices.json()

def price(): 
    for key in prices:
        data = prices[key]
        print(data['code'], ':', data['high'], ' reais.')