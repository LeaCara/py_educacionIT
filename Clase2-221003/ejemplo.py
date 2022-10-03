from hashlib import algorithms_available


def nombre(argumentos):
    #
    #
    #
    #
    return algo

def saludar():
    print("Hola, buen dia")


###############################################

saludar()

# trelent plugin
def _sumar(a=40, b=50):
    """
    The sumar function adds two numbers together and returns the result.
    
    Args:
        a (int): The first number to add.  Default value is 40.
        b (int): The second number to add.  Default value is 50.
        
    Returns:  int: The sum of a and b.
    
    :param a=40: Set the value of a to 40
    :param b=50: Set a default value for the b parameter
    :return: The sum of the two numbers that are passed as parameters
    :doc-author: Trelent
    """
    c = a + b
    print(c)

# suma
def sumar(*args):
    suma = 0
    print(f"args: {args}")
    for arg in args:
        suma = suma + arg
    print(f"suma: {suma}")

sumar(10,20,30,40)

def show(**kwargs):
    for str in kwargs:
        print(str)
        print(kwargs[str])

show(fname = "Tobias", lname = "Refsnes") 

# con un solo asterisco obtenemos una tupla y con dos asteriscos obtenemos un diccionario

# funciones de orden superior

def cuadrado(x):
    return x**2

def suma_cudrado(x, y):
    return cuadrado(x) + cuadrado(y)

print(suma_cudrado(2, 3))

# map:retorna un generador (lugar en memoria)
w = [1,2,3]
print(list(map(cuadrado, w)))

def par(x):
    return x % 2 == 0

def filtrar(func, valores):
    aux = []
    for n in valores:
        if func(n) == True:
            aux.append(n)
    return aux

w = [10,11,12,13]

# filter 
print(list(filter(par, w)))

# funcion anonima
print(list(filter(lambda x : x % 2 == 0, w)))




# Desafios practicos modulo 1 

primera = [7, 5, 10, 9, 8, 1, 3, 5, 6, 3, 8, 0, 10, 9, 2]
segunda = [6, 9, 3, 7, 9, 10, 5, 10, 7, 4, 5, 3, 2, 10, 2]

def merge(prim, sec):
    tercera = []
    for n in prim:
        for m in sec:
            if n == m:
                if n not in tercera:
                    tercera.append(n)
    print(tercera)

merge(primera, segunda)

personas = ["Susana","Tamara","Ana","Susana","Susana","Tomas","Ana"]

def dic_count(pers):
    ocurr_dict = {}
    for n in pers:
        ocurr_dict[n] = pers.count(n)
    print(ocurr_dict)

dic_count(personas)

def conversion(count):
    hh = count // 3600
    min = (count % 3600) // 60
    sec = count - hh * 3600 - min * 60
    print(f"{str(hh).zfill(2)}:{str(min).zfill(2)}:{str(sec).zfill(2)}")

conversion(6548)

