import requests

r = requests.get("https://mindicador.cl/api")
datos = r.json()
#Valor UF
uf = datos['uf']
print(uf['valor'])

#Valor del Dolar
dolar = datos['dolar']
print(dolar['valor'])
