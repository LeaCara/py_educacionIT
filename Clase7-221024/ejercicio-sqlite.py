# https://write.corbpie.com/how-to-fix-mysql-not-starting-in-xampp/#:~:text=Navigate%20to%20your%20XAMPP%20MySQL,data%20overwriting%20all%20the%20files.

# descargar pymysql y xamm

import sqlite3
import os
from tabulate import tabulate 

conn = sqlite3.connect("comercio.sqlite")
cursor = conn.cursor()

try:
    cursor.execute("CREATE TABLE productos (id INT,nombre TEXT,precio INT)")
    print("Bienvenido")
except sqlite3.OperationalError:
    print("Bienvenido nuevamente")

lista_productos = [[1,"Teclado",10],[10,"Mouse",10],[3,"Parlantes",15],[4,"Monitor",100]]

for n in lista_productos:
    cursor.execute("INSERT INTO productos (?,?,?)",(n[0],n[1],n[2]))




def leer():
    conn = sqlite3.connect("comercio.sqlite")
    cursor = conn.cursor()
    cursor.execute("SELECT")