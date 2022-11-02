import tkinter as tk
from tkinter import messagebox
import sys


######################################################

def convertir(dato):
    try:
        dato = float(dato)
    except ValueError:
        dato = "error"
    return dato


def sumar():
    ctres.delete(0, tk.END)
    a = cuno.get()
    a = convertir(a)
    b = cdos.get()
    b = convertir(b)
    if a != "error" and b != "error":
        c = a + b
    else:
        c = "error"
    ctres.insert(0, c)


def restar():
    ctres.delete(0, tk.END)
    a = cuno.get()
    a = convertir(a)
    b = cdos.get()
    b = convertir(b)
    if a != "error" and b != "error":
        c = a - b
    else:
        c = "error"
    ctres.insert(0, c)


def multiplicar():
    ctres.delete(0, tk.END)
    a = cuno.get()
    a = convertir(a)
    b = cdos.get()
    b = convertir(b)
    if a != "error" and b != "error":
        c = a * b
    else:
        c = "error"
    ctres.insert(0, c)


def dividir():
    ctres.delete(0, tk.END)
    a = cuno.get()
    a = convertir(a)
    b = cdos.get()
    b = convertir(b)
    if a != "error" and b != "error":
        try:
            c = a / b
        except ZeroDivisionError:
            c = "error"
    else:
        c = "error"
    ctres.insert(0, c)


def informar():
    messagebox.showinfo(title="Info de la App",
                        message="Aplicacion creada en el curso PyProg")


def salir():
    r = messagebox.askokcancel(
        title="A punto de salir", message="¿Esta seguro de salir?")
    if r:
        sys.exit()


######################################################
ventana = tk.Tk()
ventana.config(width=300, height=300)
ventana.title("Calculadora")


etuno = tk.Label(text="Dato uno:")
etuno.place(x=20, y=20)
cuno = tk.Entry()
cuno.place(x=20, y=50)

etdos = tk.Label(text="Dato dos:")
etdos.place(x=160, y=20)
cdos = tk.Entry()
cdos.place(x=160, y=50)


bsuma = tk.Button(text="  +  ", command=sumar)
bsuma.place(x=25, y=100, width=30)

brestar = tk.Button(text="  -  ", command=restar)
brestar.place(x=95, y=100, width=30)

bmult = tk.Button(text="  x  ", command=multiplicar)
bmult.place(x=165, y=100, width=30)

bdiv = tk.Button(text="  /  ", command=dividir)
bdiv.place(x=245, y=100, width=30)

ettres = tk.Label(text="Resultado:")
ettres.place(x=80, y=160)
ctres = tk.Entry()
ctres.place(x=80, y=190)

binfo = tk.Button(text="info", command=informar)
binfo.place(x=40, y=230, width=80, height=50)

binfo = tk.Button(text="Salir", command=salir)
binfo.place(x=160, y=230, width=80, height=50)

ventana.mainloop()
