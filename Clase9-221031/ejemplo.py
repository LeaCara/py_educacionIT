import tkinter as tk

def presionado():
    csaludo.delete()
    nombre = caja.get()
    #print("Hola", nombre)
    frase = "Hola " + nombre
    csaludo.insert(0,frase)
 
ventana = tk.Tk()

ventana.config(width=300, height=300)
ventana.title("Mi app")

boton = tk.Button(text="Hola")

boton.place(x=20, y=20)

caja = tk.Entry()
caja.place(x=20, y=120)

etiqueta = tk.Label(text="Ingrese su nombre: ")
etiqueta.place(x=20, y=90)

ventana.mainloop()