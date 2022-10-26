import requests
from flask import Flask
# install flask
#  beautiful so  es mejor que request para traer datos del servidor

datos = {
    "name": "Mariano",
    "email": "mariano@ejemplo.com",
    "message":"¡Hola, mundo!"
}

r = requests.post("http://localhost:8880/form", data=datos)