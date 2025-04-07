"""""

1) Almacenamiento de Productos Ecologicos
2) Informacion detallada sobre los Productos Ecologicos(Beneficios,Donde Comprar,etc)
3) Busqueda de Productos Ecologicos por Categorias 

4) Clasificacion por Categoria de los Prodcutos
    Alimentos Organicos (Frutas, Verduras, Cereales y Productos sin Quimicos)
    Productos de Higiene y Cosmetica (Jabones, Champus y Crenas Biodegradables)
    Alternativas Sostenibles (Botellas Reutilizables, Bolsas de Tela, Pitillos de Bambu, etc)
    Productos de Limpieza Ecologicos (Detergentes sin Quimicos agresivos, Esponjas Biodegradables)

5) Generar Conciencia
    -> Informacion sobre el impacto del uso de productos quimicos en la salud y el medio ambiente
        
FUNCIONALIDAD_P

1) Permite ingresar un nuevo producto en una de las categorias -LISTO
2) Muestra la lista de productos de una categoria especifica - LISTO
3) Verificar si un producto esta registrado en el sistema 
4) Borrar un producto especifico de la base de datos
5) Perimite modificar los detalles de un producto
6) Permite visualizar todos los productos ecologicos 

7) Clasificacion Segun impacto ambiental
    Alto Impacto (Requiere Mejoras para ser mas Ecologico)
    Medio Impacto (Sostenible, pero con Margen de Mejora)
    Bajo Impacto (Totalmente ecologico y biodegradable)

8) Salir del sistema

"""""

print('Bienvenido al Programa de Consultas sobre Productos Ecologicos'.center(70, '-'))

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
    (4) Modificar Productos
    (5) Ver Productos
    (6) Salir del Programa
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
    


    


