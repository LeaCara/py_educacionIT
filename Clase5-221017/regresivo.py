import sys
import time

argumentos = sys.argv

ayuda = """
Ayuda del programa regresiva.py

Este es un programa que admite un argumento <int>
Y realiza una cuenta atras desde ese valor hasta 0 (cero)

Ejemplo:
/regresiva.py 5
>>>5
>>>4
>>>3
>>>2
>>>1
>>>0

"""

try:
    valor = argumentos[1]
    try:
        valor = int(valor)
    except ValueError:
        if valor.lower() == "-h" or valor.lower() == "-help":
            print(ayuda)
        else:
            print("No es un número")
        print("Error no se puede convertir")
except IndexError:
    print("Faltan argumentos")
    sys.exit()