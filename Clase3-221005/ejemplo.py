# excepciones
while True:
    try:
        edad = int(input("hay un ingreso")) # siempre conviene desglosar, no hacer en misma linea
        break
    except:
        print("hay un error en el ingreso")

if edad < 18: 
    print("Edad menor")

def ingreso_numeros(mensaje):
    while True:
        dato = input(mensaje)
        try:
            dato = int(dato)
            break
        except ValueError:
            try:
                dato = float(dato)
                break
            except ValueError:
                print("Hay un error con el ingreso. Intente nuevamente.")
    return dato


def ingreso_numeros(mensaje):
    while True:
        dato = input(mensaje)
        try:
            dato = int(dato)
        except ValueError:
            print("No entero")

def sumar(a,b):
    if not isinstance(a,(int,float)) or not isinstance(b,(int,float)):
        raise TypeError("Son datos que no corresponde al uso de la función")
    else:
        c = a + b
        print(c)

def sumar(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Se requieren dos numeros.")
    return a + b
print(sumar(7, 5)) #Imprime 12.
#out: 12
print(sumar(2.5, 3.5)) # Imprime 6.
#out: 6.0
#print(sumar([1, 2], [3, 4])) # Lanza la excepción.
##out:
#raise TypeError("Se requieren dos numeros.")
# TypeError: Se requieren dos numeros.

# Operaciones sobre strings


# Manejo de archivos

f = open("data.txt")
texto = f.readlines()
f.close()

print(texto)



