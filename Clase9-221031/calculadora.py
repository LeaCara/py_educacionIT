# modulo tkinter

import tkinter as tk
tkinter.messagebox

def sumar():
    ctres.delete(0, tk.END)
    a = cuno.get()
    a = convertir(a)

def informar():


bsuma = tk.Button(text="   +   ", command=sumar)
bsuma.place(x=25, y=100, width=30)


brestar.place(x=95, y=100, width=30)

bmult = tk.Button(text="   x   ")
bmult.place(x=165, y=100, width=30)

bdiv = tx.Button(text="   /   ")
bdiv.place(x=245, y=100, width=30)

ettres = tk.Label(text="Resultado:")
ettres.place(x=80, y=160)
cajatres = tk.Entry()
cajatres.place(x=80, y=190)

binfo = tk.Button(text="info")

binfo.place(x=40, y=230)

ventana.mainloop()