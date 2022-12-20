import requests
import os
import time


while True:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    datos = r.json()

    bpi = datos['bpi']
    usd = bpi['USD']
    valor = usd['rate']
    os.system("cls")
    print(f"El valor del Bitcoin al momento es: USD $ {valor}")
    time.sleep(10)