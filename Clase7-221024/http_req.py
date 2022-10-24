# https://github.com/Castrogiovanni20/api-dolar-argentina
# https://api-dolar-argentina.herokuapp.com/api/dolaroficial

import requests

r = requests.get("https://api-dolar-argentina.herokuapp.com/api/dolaroficial")
r.json()

d = r.json()
print(d["venta"])
