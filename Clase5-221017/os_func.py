"""

- os.getcwd()
Me devuelve el directorio donde estoy

- os.mkdir()
Permite crear una carpeta

- os.path.exists()
Devuelve un estado booleano, si existe un directorio True
Si no existe False

- os.rename()
Me permite cambiar el nombre del archivo.

- os.remove()
Permite eliminar archivos de un directorio

- os.rmdir()
permite eliminar directorio vacios

- os.system()
Permite ejecutar comandos de consola 
(mucho más potente subproces, otro modulo)

- os.name

"""
import os

os.rename("regresiva.py", "cuenta_atras.py")

if os.name == "nt":  # Windows es 'nt'
    borrar = "cls"
else:
    borrar = "clear"

os.system(borrar)

