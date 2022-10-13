import time

def guardar(n, fech, eve):
    f = open("registro.txt", "a")
    f.write(f"{n} - {e} - {fech}\n")
    f.close()
    print("Evento guardado")


###########################################

while True:
    print("""
    1 - Ingreso
    2 - Egreso
    3 - Salir del sistema    
    """)
    opcion = input("Ingrese opcion: ")
    if opcion == "1":
        nombre = input("Nombre: ")
        evento = "ingreso"
        fecha = time.asctime()
        guardar(nombre, fecha, evento)
    elif opcion == "2":
        nombre = input("Nombre: ")
        evento = "egreso"
        fecha = time.asctime()
        guardar(nombre, fecha, evento)
    elif opcion == "3":
        print("Saliendo...")
