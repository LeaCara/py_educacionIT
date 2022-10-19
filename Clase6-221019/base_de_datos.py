"""
Base de datos



MySQL
MariaDB
Oracle
Sql Server
Big Query


SQLite -> Motor de base de datos que puede acceder a base de datos y simular un servidor utilizando un archivo
no permite multiples conexiones (es un archivo), no debe dejarse este motor. 



"""

# descargar sqlite browser: visor de base de datos

import sqlite3

conn = sqlite3.connect("cursos.sqlite")
cursor = conn.cursor()

try:
    cursor.execute("CREATE TABLE alumnos (nombre TEXT,edad INT)")
    print("Bienvenido")
except sqlite3.OperationalError:
    print("Bienvenido nuevamente")

nombre = input()
edad = input()

cursor.execute("INSERT INTO alumnos VALUES (?,?)",(nombre,edad))

