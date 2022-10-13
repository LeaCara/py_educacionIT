encargado = ""
l_encargado = ["Gerardo", "Roberto", "Fernando"]
error = True
while error:
    print("Bienvenido a Hamburguesas IT")
    input("Ingrese su nombre encargad@:")
    if not encargado in l_encargado:
        error = True
        print("Encargado inexistente")
    else:
        error = False

    
