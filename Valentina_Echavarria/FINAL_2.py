

print('Bienvenido al Programa de Consultas sobre Productos Ecologicos')
#Creacion de las Listas Basicas
productos = []



#Agregar productos a una Categoria Especiica
alimentos_orga = ['uva', 'naranja', 'piña', 'plátano', 'fresa', 'pimiento', 'berenjena', 'ajo', 'cebolla', 'arroz integral', 
 'maíz', 'trigo sarraceno', 'manzana', 'pera', 'mango', 'papaya', 'kiwi', 'cereza', 'durazno', 'zanahoria', 
 'coliflor', 'repollo', 'apio', 'jengibre', 'cebada', 'centeno', 'espelta', 'mijo', 'melón', 'sandía', 'granada', 
 'brócoli', 'espinaca', 'lechuga', 'pepino', 'rábano', 'calabacín', 'avena', 'quinoa', 'amaranto', 'harina de coco']



productos_hc = ['jabón protex', 'champú head & shoulders', 'crema vaseline', 'desodorante axe', 'enjuague listerine', 
 'toallitas huggies', 'detergentes', 'disolventes', 'plaguicidas', 'jabón dove', 'champú pantene', 'crema nivea', 
 'desodorante rexona', 'enjuague colgate', 'toallitas reutilizables', 'jabón biodegradable', 'vinagre', 'bicarbonato de sodio', 
 "jabón dr. bronner's", 'champú lush', 'crema weleda', "desodorante schmidt's", 'enjuague georganics', 'toallitas de algodón']


alterna_sos = ['botellas de plástico desechables', 'bolsas de plástico', 'pajillas de plástico',
 'cubiertos de plástico', 'envases de poliestireno', 'film plástico para envolver alimentos',
 'botellas de plástico reciclable', 'bolsas reutilizables sintéticas', 'pajillas de papel',
 'cubiertos de bambú desechables', 'envases de cartón con recubrimiento', 'papel encerado biodegradable',
 'botellas de acero inoxidable', 'bolsas de tela', 'pajillas de bambú',
 'cubiertos de acero inoxidable', 'envases de vidrio reutilizables', 'cera de abeja para envolver alimentos']


productos_limE = ['detergentes con fosfatos', 'lejía con cloro', 'desengrasantes químicos agresivos',
 'limpiadores con amoníaco', 'blanqueadores industriales', 'removedores de óxido químicos',
 'detergentes con fragancias sintéticas', 'limpiadores multiusos con químicos moderados', 'esponjas con microfibras sintéticas',
 'desinfectantes con alcohol', 'suavizantes de telas convencionales', 'lavaplatos con tensoactivos sintéticos',
 'detergentes ecológicos sin fosfatos', 'jabón de castilla', 'esponjas biodegradables de luffa', 'vinagre blanco', 'bicarbonato de sodio',
 'percarbonato de sodio', 'ácido cítrico', 'aceites esenciales desinfectantes', 'jabón negro líquido', 'ceniza de madera para limpieza natural']


while True:
    print("""
    (1) Añadir Productos
    (2) Buscar Productos por Categoria
    (3) Verificar Exsistencia de un Producto
    (4) Eliminar un Producto
    (5) Ver Productos Ecologicos
    (6) Salir del Programa
    """)

    opcion = int(input('Ingrese la Opcion: '))

    # Pedir Datos de las Listas
    if opcion == 1:
        an_productos = input('Ingrese el Nombre del Producto: ').lower()
        productos.append(an_productos)


        an_categoria = int(input('Ingrese el Numero de la Categoria del Producto: ' 
                             """

        (1) Alimentos Organicos
        (2) Productos de Higiene y Cosmetica 
        (3) Alternativas Sostenibles
        (4) Productos de Limpieza Ecologicos
            """))

        if an_categoria == 1:
            an_categoria = 'Alimentos Organicos'

            alimentos_orga.append(an_productos)


        elif an_categoria == 2:
            an_categoria = 'Productos de Higiene y Cosmetica'

            productos_hc.append(an_productos)


        elif an_categoria == 3:
            an_categoria = 'Alternativas Sostenibles'

            alterna_sos.append(an_productos)


        elif an_categoria == 4:
            an_categoria = 'Productos de Limpieza Ecologicos'

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
            print(F"Los Productos Organicos son: {alimentos_orga} ")
        elif buscador == 2:
            print(F"Los Productos de Higiene y Cosmetica son: {productos_hc} ")
        elif buscador == 3:
            print(F"Los Productos Alternativas Sostenibles son: {alterna_sos} ")
        elif buscador == 4:
            print(F"Los Productos de Limpieza Ecologicos son: {productos_limE} ")
        else:
            print('Categoria No Valida')
 
    # Verificar Existencias
    elif opcion == 3:
        buscador = input('Ingrese el Producto a Buscar: ').lower()
        if buscador in productos:

            print('El Producto si existe')
        else:
            print("Producto no encontrado")

    # Borrar Producto Especifico de la Base de datos
    elif opcion == 4:
        buscador = input('Ingrese el Producto a Eliminar: ').lower()
        if buscador in productos:
            posicion = productos.index(buscador)
            productos.pop(posicion)


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

    # Ver Todos Los Productos Ecologicos
    elif opcion == 5:
        print("\nLos Productos Orgánicos son:\n" + "\n".join(alimentos_orga) + "\n")
        print("Los Productos de Higiene y Cosmética son:\n" + "\n".join(productos_hc) + "\n")
        print("Las Alternativas Sostenibles son:\n" + "\n".join(alterna_sos) + "\n")
        print("Los Productos de Limpieza Ecológicos son:\n" + "\n".join(productos_limE) + "\n")

    # Salir
    elif opcion == 6:
        print("""
                        ¡Un pequeño cambio, un gran impacto! 
    Al utilizar productos ecológicos, puedes reducir la emisión de gases de efecto invernadero 
            en un 25% y disminuir la contaminación del agua en un 40%. 
    ¡Haz la diferencia y elige productos ecológicos para un futuro más verde y saludable!
        """)
        break
    else:
        print("Opción inválida. Por favor, inténtelo de nuevo.")
    
