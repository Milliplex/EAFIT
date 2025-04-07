
#Creacion de las Listas Basicas

productos = []
categorias = []
detalles_produc = []

alimentos_orga = []
productos_hc = []
alterna_sos = []
productos_limE = []

while True:
    print("""
    (1) Añadir Productos
    (2) Buscar Productos por Categoria
    (3) Verificar Exsistencia de un Producto
    (4) Eliminar un Producto
    (5) Salir del Programa
    """)

    opcion = int(input('Ingrese la Opcion: '))

    # Pedir Datos de las Listas
    if opcion == 1:
        an_productos = input('Ingrese el Nombre del Producto: ')
        productos.append(an_productos)

        dt_productos = input('Ingrese detalles de su Producto: ')
        detalles_produc.append(dt_productos)

        an_categoria = int(input('Ingrese el Num de la Categoria del Producto: ' 
                             """
        (1) Alimentos Organicos
        (2) Productos de Higiene y Cosmetica 
        (3) Alternativas Sostenibles
        (4) Productos de Limpieza Ecologicos
            """))

        if an_categoria == 1:
            an_categoria = 'Alimentos Organicos'
            categorias.append(an_categoria) 
            alimentos_orga.append(an_productos)

        elif an_categoria == 2:
            an_categoria = 'Productos de Higiene y Cosmetica'
            categorias.append(an_categoria)
            productos_hc.append(an_productos)


        elif an_categoria == 3:
            an_categoria = 'Alternativas Sostenibles'
            categorias.append(an_categoria)
            alterna_sos.append(an_productos)

        elif an_categoria == 4:
            an_categoria = 'Productos de Limpieza Ecologicos'
            categorias.append(an_categoria)
            productos_limE.append(an_productos)

    # Buscar Productos por Categoria
    elif opcion == 2:
        buscador = int(input('Que Productos de que Categoria desea visualizar: ' 
                             """
        (1) Alimentos Organicos
        (2) Productos de Higiene y Cosmetica 
        (3) Alternativas Sostenibles
        (4) Productos de Limpieza Ecologicos
            """))
        if buscador == 1:
            print('Los Productos Organicos son: ', alimentos_orga)
        elif buscador == 2:
            print('Los Productos de Higiene y Cosmetica son: ', productos_hc)
        elif buscador == 3:
            print('Las Alternativas Sostenibles son: ', alterna_sos)
        elif buscador == 4:
            print('Los Productos de Limpieza Ecologicos son: ', productos_limE)
        else:
            print('Categoria No Valida')

    
    # Verificar Existencias
    elif opcion == 3:
        buscador = input('Ingrese el Producto a Buscar: ')
        if buscador in productos:
            posicion = productos.index(buscador)
            print('El Producto si existe')
        else:
            print("Producto no encontrado")

    # Borrar Producto Especifico de la Base de datos
    elif opcion == 4:
        buscador = input('Ingrese el Producto a Eliminar: ')
        if buscador in productos or  alimentos_orga or productos_hc or alterna_sos or productos_limE:
            posicion = productos.index(buscador)
            productos.pop(posicion)
            categorias.pop(posicion)

            if buscador in alimentos_orga:
                alimentos_orga.pop(posicion)
            elif buscador in productos_hc:
                productos_hc.pop(posicion)
            elif buscador in alterna_sos:
                alterna_sos.pop(posicion)
            elif buscador in productos_limE:
                productos_limE.pop(posicion)

        
            print('Producto Eliminado')
        else:
            print("Producto no encontrado")

    # Salir
    elif opcion == 5:
        print("""
        ¡Un pequeño cambio, un gran impacto! 
        Al utilizar productos ecológicos, puedes reducir la emisión de gases de efecto invernadero en un 25% y disminuir la contaminación del agua en un 40%. 
        ¡Haz la diferencia y elige productos ecológicos para un futuro más verde y saludable!
        """)
        break
    else:
        print("Opción inválida. Por favor, inténtelo de nuevo.")
    