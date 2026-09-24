nombres = []
telefonos = []
Emails = []
direcciones = []

contactos = {}

while True: 
    menu = """ 

    ### ELIJE UNA OPCION ###

    1. agregar un contacto 
    2. buscar un contacto 
    3. eliminar un contacto
    4. Ver Contactos
    5. Salir
    """
    opcion_elegida = int(input(menu))

    if opcion_elegida == 1:
        nombre = input("ingrese el nombre:")
        nombre = nombre.lower()
        telefono = input("ingrese el telefono:")
        email = input("ingrese su email:")
        direccion = input("ingresa su direccion")
        contactos[nombre] = {
            "telefono": telefono,
            "email": email,
            "direccion": direccion
        }
        print(f"contacto {nombre} guardado exitosamente")
    elif opcion_elegida ==2: 
        nombre = input("ingrese el nombre a buscar:").lower()
        if nombre in contactos:
            print("=*10")
            print(contactos[nombre])
            print("=*10")
        else:
            print("El contacto no existe")

    elif opcion_elegida ==3: 
        nombre = input("ingrese el nombre a eliminar: ").lower()
        if nombre in contactos:
            del contactos[nombre]
            print(f"contacto {nombre} eliminado exitosamente")
        else:
            print(f"Contacto {nombre} no registrado")
    elif opcion_elegida ==4:
        for i, key in enumerate(contactos):
            print(i+1,"-",key)
    elif opcion_elegida ==5: 
        print("Gracias por usar la agenda de contactos")
        break
    else:
        print("Opcion no valida, intente de nuevo")