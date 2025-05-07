"""""

1) Almacenamiento de Productos Ecologicos
2) Informacion detallada sobre los Productos Ecologicos(Beneficios,Donde Comprar,etc)
3) Busqueda de Productos Ecologicos por Categorias 

4) Clasificacion por Categoria de los Prodcutos
    Alimentos Organicos (Frutas, Verduras, Cereales y Productos sin Quimicos)
    Productos de Higiene y Cosmetica (Jabones, Champus y Crenas Biodegradables)
    Alternativas Sostenibles (Botellas Reutilizables, Bolsas de Tela, Pitillos de Bambu, etc)
    Productos de Limpieza Eco (Detergentes sin Quimicos agresivos, Esponjas Biodegradables)

5) Generar Conciencia
    -> Informacion sobre el impacto del uso de productos quimicos en la salud y el medio ambiente
        
FUNCIONALIDAD_P

1) Permite ingresar un nuevo producto en una de las categorias
2) Muestra la lista de productos de una categoria especifica 
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

while True:
    print("""
    (1) Añadir Productos
    (2) Buscar Productos
    (3) Modificar Productos
    (4) Ver Productos
    (5) Salir del Programa
    """)

    opcion = int(input('Ingrese la Opcion: '))

    # Pedir Datos de las Listas
    if opcion == 1:
        an_productos = input('Ingrese el Nombre de su Producto ')
        
        # Agregar a la Lista
        productos.append(an_productos)

    # Buscar Productos
    elif opcion == 2:
        buscador = input('Ingrese el Nombre del Producto que quiere Buscar: ')
        if buscador in productos:
            posicion = productos.index(buscador)
            print('El Nombre del Producto es: ', productos[posicion])
        else:
            print("Producto no encontrado")

    # Modificar Productos
    elif opcion == 3:
        buscador = input('Ingrese el Nombre del Producto que quiere Modificar: ')
        if buscador in productos:
            posicion = productos.index(buscador)
            an_productos = input('Ingrese el Nombre de su Producto ')
            productos[posicion] = an_productos
        else:
            print("Producto no encontrado")

    # Ver Productos
    elif opcion == 4:  
        print('El Nombre del Producto es: ', productos)

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
    


    


