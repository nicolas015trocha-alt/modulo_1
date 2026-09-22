nombres = []
telefonos = []
Emails = []
direcciones = []

while True: 
    menu = """ 

    ### ELIJE UNA OPCION ###

    1. agregar un contacto 
    2. buscar un contacto 
    3. eliminar un contacto
    4. salir
    """
    opcion_elegida = int(input(menu))

    if opcion_elegida == 1:
        nombre = input("ingrese el nombre:")
        telefono = input("ingrese el telefono:")
        email = input("ingrese su email:")
        direccion = input("ingresa su direccion")

        nombres.append(nombre)
        telefonos.append(telefono)
        direcciones.append(email)

        print(f"contacto(nombre) guardado exitosamente")
    elif opcion_elegida ==2: 
        nombre = input("ingrese el nombre a buscar:")
        if nombre in nombres:
            indice = nombres.index(nombre)
            print("="*10)
            print(f"nombre: {nombres[indice]}")
            print(f"telefono: {telefonos[indice]}")
            print(f"email: {Emails[indice]}")
            print(f"direccion: {direcciones[indice]}")
            print("="*10)        
    elif opcion_elegida ==3: 
        pass
    elif opcion_elegida ==4:
        for nombre, telefono,mail,direccion in zip(nombres,telefonos,Emails,direcciones):
            print(f"nombre:{nombre}")
            print(f"telefono:{telefono}")
            print(f"Email: {email}")
            print(f"direccion:{direccion}")
    else: 
        print("opcion invalida")