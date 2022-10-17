class Ejemplo:
    def __init__(self):
        self.valor = 10
        self.__color = "Rojo"
    
    def __secret(self):
        print('Nadie puede saber!')

    def get(self):
        print(self.__color)
    
    def set(self,param):
        self.__color = param 

    def ejecutar(self):
        self.__secret()


#############################################

obj = Ejemplo()

#print(obj.__color) # Lo dejo comentado porque es un error! Att Privado

obj.get() #Rojo
obj.set("Amarillo")
obj.get() #Amarillo
#obj.__secret() #lo dejo comentado es un error! Met Privado
obj.ejecutar() # Nadie puede saber!