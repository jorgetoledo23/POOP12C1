#pip install requests

import requests

r = requests.get("https://catfact.ninja/fact")
datos = r.json()
print(datos['fact'])
