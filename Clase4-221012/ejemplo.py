"""
Paradigma:
es una forma de resolver un problema en programación


POO


Entidades=
*Atributos: características
*Metodos: funcionalidades


Ejemplo de la vida real
celular:
*Color(atributo) -> Negro
*LLamar(metodo) -> hace algo

"""

from tkinter import Tk
import time

class Nombre():
    def __init__(self):
        self.color = "Rojo"
        self.material = "Plastico"

    def picar(self):
        print("pim pam pum")


#################################################################
        

class Cliente():
    def __init__(self, nom=None, documento=None):
        self.nombre = nom
        self.dni = documento
        self.desde = int(time.asctime().split()[-1])

    def comprar(self, item, valor):
        print(f"{self.nombre} compra:{item} a ${valor}")

    def promocion(self):
        if self.desde < 2023:
            print("Tiene promo asociada")
        else:
            print("No tiene promo")
#################################################################

a = Cliente()

a.nombre = "Nacho"
a.dni = "48000000"

print(a.nombre)


# Laboratorio
class Persona():
    def __init__(self, nom=None, edad=None):
        self.nombre = nom
        self.edad = edad
        
    def cumpleaños(self):
        self.edad += 1

p = Persona("Juan", 21)
print(f"{p.nombre} cumple {p.edad} años")
p.cumpleaños()
print(f"{p.nombre} cumple {p.edad} años")


# atributos privados

class Persona():
    def __init__(self, nom=None, edad=None):
        self.__nombre = nom
        self.__edad = edad
    
    def set(self, nom):
        self.__nombre = nom
        
    def get(self):
        return self.__nombre
        
    def cumpleaños(self):
        self.__edad += 1


# herencia de clases
class ClaseA:
    def __init__(self):
        self.a = 1

class ClaseC:
    def __init__(self):
        pass


# class ClaseB(ClaseA):
#     def __init__(self):
#         super().__init__()   # se debe llamar explicitamente al constructor de la clase padre para que se utilice
#         self.b = 2

class ClaseB(ClaseA, ClaseC):  #multiples clases
    def __init__(self):
        ClaseA.__init__()   # se debe llamar explicitamente al constructor de la clase padre para que se utilice
        ClaseC.__init__()   # se debe llamar explicitamente al constructor de la clase padre para que se utilice
        self.b = 2