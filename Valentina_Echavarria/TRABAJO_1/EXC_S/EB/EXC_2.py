
cantidad = []
productos = []
precio = []


while True:
    print("""
    (1) Añadir Productos
    (2) Buscar Productos
    (3) Modificar Productos
    (4) Ver Productos
    (5) Salir
    """)
    respuesta = int(input('Ingrese su Opcion: '))

    # Pedir Datos de las Listas
    if respuesta == 1:
        ac = int(input('Ingrese la Cantidad de su Producto '))
        ap = input('Ingrese el Nombre de su Producto ')
        apre = int(input('Ingrese el Precio de Su Producto '))
        # Agregar a la Lista
        cantidad.append(ac)
        productos.append(ap)
        precio.append(apre)

    # Buscar Productos
    elif respuesta == 2:
        buscador = input('Ingrese el Nombre del Producto que quiere Buscar: ')
        if buscador in productos:
            posicion = productos.index(buscador)
            print('La Cantidad del Producto es: ', cantidad[posicion])
            print('El Nombre del Producto es: ', productos[posicion])
            print('El Precio del Producto es: ', precio[posicion])
        else:
            print("Producto no encontrado")

    # Modificar Productos
    elif respuesta == 3:
        buscador = input('Ingrese el Nombre del Producto que quiere Modificar: ')
        if buscador in productos:
            posicion = productos.index(buscador)
            ac = int(input('Ingrese la Cantidad de su Producto '))
            ap = input('Ingrese el Nombre de su Producto ')
            apre = int(input('Ingrese el Precio de Su Producto '))
            cantidad[posicion] = ac
            productos[posicion] = ap
            precio[posicion] = apre
        else:
            print("Producto no encontrado")

    # Ver Productos
    elif respuesta == 4:
        print('La Cantidad es: ', cantidad)
        print('El Nombre del Producto es: ', productos)
        print('El Precio es: ', precio)

    # Salir
    elif respuesta == 5:
        print('Gracias por Utilizar el Programa')
        break
    else:
        print("Opción inválida. Por favor, inténtelo de nuevo.")