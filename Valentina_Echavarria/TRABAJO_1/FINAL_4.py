
print('Bienvenido al Programa de Consultas sobre Productos Ecologicos')

#Lista de Productos Segun su Categoria
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

#Base de Datos de Productos Segun su Impacto Ambiental
alto_impacto = ('uva', 'naranja', 'piña', 'plátano', 'fresa', 'pimiento', 'berenjena', 'ajo', 'cebolla', 'arroz integral', 
 'maíz', 'trigo sarraceno', 'pesticidas', 'fertilizantes sintéticos', 'herbicidas', 'jabón protex', 'champú head & shoulders', 
 'crema vaseline', 'desodorante axe', 'enjuague listerine', 'toallitas huggies', 'botellas de plástico desechables', 'bolsas de plástico', 
 'pajillas de plástico', 'cubiertos de plástico', 'envases de poliestireno', 'film plástico', 'detergentes con fosfatos', 'lejía con cloro', 
 'desengrasantes químicos agresivos', 'limpiadores con amoníaco', 'blanqueadores industriales', 'removedores de óxido químicos')

medio_impacto = ('manzana', 'pera', 'mango', 'papaya', 'kiwi', 'cereza', 'durazno', 'zanahoria', 'coliflor', 'repollo', 
 'apio', 'jengibre', 'cebada', 'centeno', 'espelta', 'mijo', 'detergentes', 'disolventes', 'plaguicidas', 
 'jabón dove', 'champú pantene', 'crema nivea', 'desodorante rexona', 'enjuague colgate', 'toallitas reutilizables', 
 'botellas de plástico reciclable', 'bolsas reutilizables sintéticas', 'pajillas de papel', 
 'cubiertos de bambú desechables', 'envases de cartón con recubrimiento', 'papel encerado biodegradable', 
 'detergentes con fragancias sintéticas', 'limpiadores multiusos con químicos moderados', 'esponjas con microfibras sintéticas', 
 'desinfectantes con alcohol', 'suavizantes de telas convencionales', 'lavaplatos con tensoactivos sintéticos')

bajo_impacto = ('melón', 'sandía', 'granada', 'brócoli', 'espinaca', 'lechuga', 'pepino', 'rábano', 'calabacín', 
 'avena', 'quinoa', 'amaranto', 'harina de coco', 'jabón biodegradable', 'vinagre', 'bicarbonato de sodio',
 "jabón dr. bronner's", 'champú lush', 'crema weleda', "desodorante schmidt's", 'enjuague georganics', 
 'toallitas de algodón', 'botellas de acero inoxidable', 'bolsas de tela', 'pajillas de bambú',
 'cubiertos de acero inoxidable', 'envases de vidrio reutilizables', 'cera de abeja para envolver alimentos', 
 'detergentes ecológicos sin fosfatos', 'jabón de castilla', 'esponjas biodegradables de luffa', 'vinagre blanco', 
 'bicarbonato de sodio', 'percarbonato de sodio', 'ácido cítrico', 'aceites esenciales desinfectantes', 
 'jabón negro líquido', 'ceniza de madera para limpieza natural')


while True:
    print("""
    (1) Añadir Productos
    (2) Buscar Productos por Categoria
    (3) Verificar Exsistencia de un Producto
    (4) Eliminar un Producto
    (5) Ver Productos Ecologicos
    (6) Buscar Productos y Saber Su Impacto Ambiental      
    (7) Salir del Programa
    """)

    opcion = int(input('Ingrese la Opcion: '))

    # Pedir Datos de las Listas
    if opcion == 1:
        nuevo_producto = input('Ingrese el Nombre del Producto: ').lower()

        agregar_categoria = int(input('Ingrese el Numero de la Categoria a la que Pertence el Producto: ' 
                             """

        (1) Alimentos Organicos
        (2) Productos de Higiene y Cosmetica 
        (3) Alternativas Sostenibles
        (4) Productos de Limpieza Ecologicos
            """))

        if agregar_categoria == 1:
            agregar_categoria = 'Alimentos Organicos'
            alimentos_orga.append(nuevo_producto)

        elif agregar_categoria == 2:
            agregar_categoria = 'Productos de Higiene y Cosmetica'
            productos_hc.append(nuevo_producto)

        elif agregar_categoria == 3:
            agregar_categoria = 'Alternativas Sostenibles'
            alterna_sos.append(nuevo_producto)


        elif agregar_categoria == 4:
            agregar_categoria = 'Productos de Limpieza Ecologicos'
            productos_limE.append(nuevo_producto)

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
            print("Los Productos Organicos son:" ,alimentos_orga)
        elif buscador == 2:
            print("Los Productos de Higiene y Cosmetica son: " ,productos_hc)
        elif buscador == 3:
            print("Los Productos Alternativas Sostenibles son: " ,alterna_sos)
        elif buscador == 4:
            print("Los Productos de Limpieza Ecologicos son: " ,productos_limE)
        else:
            print('Categoria No Valida')
 
    # Verificar Existencias
    elif opcion == 3:
        producto_a_buscar = input('Ingrese el Producto a Buscar: ').lower()
        if producto_a_buscar in alimentos_orga:
            print('El Producto si existe')
        elif producto_a_buscar in productos_hc:
            print('El Producto si existe')
        elif producto_a_buscar in alterna_sos:
            print('El Producto si existe')
        elif producto_a_buscar in productos_limE:
            print('El Producto si existe')
        else:
            print("Producto no encontrado")

    # Borrar Producto Especifico de la Base de datos
    elif opcion == 4:
        producto_a_eliminar = input('Ingrese el Producto a Eliminar: ').lower()
    
        if producto_a_eliminar in alimentos_orga:
            alimentos_orga.remove(producto_a_eliminar)
            print('Producto Eliminado')

        elif producto_a_eliminar in productos_hc:
            productos_hc.remove(producto_a_eliminar)
            print('Producto Eliminado')

        elif producto_a_eliminar in alterna_sos:
            alterna_sos.remove(producto_a_eliminar)
            print('Producto Eliminado')

        elif producto_a_eliminar in productos_limE:
            productos_limE.remove(producto_a_eliminar)
            print('Producto Eliminado')

        else:
            print("Producto no encontrado")

    # Ver Todos Los Productos Ecologicos
    elif opcion == 5:
        print('Los Productos Orgánicos son:\n', alimentos_orga, "\n")  
        print('Los Productos de Higiene y Cosmética son:\n', productos_hc, "\n")  
        print('Las Alternativas Sostenibles son:\n', alterna_sos,)  
        print('Los Productos de Limpieza Ecológicos son:', productos_limE, )  

    # Buscar Productos y saber su Impacto Ambiental
    elif opcion == 6:
        buscador = input('Ingrese el Producto a Buscar: ').lower()
    
        if buscador in alto_impacto:
            print('El Producto es de: Alto Impacto Ambiental')
        elif buscador in medio_impacto:
            print('El Producto es de: Medio Impacto Ambiental')
        elif buscador in bajo_impacto:
            print('El Producto es de: Bajo Impacto Ambiental')
        else:
            print('No se encontró la información')

    # Salir
    elif opcion == 7:
        print("""
                        ¡Un pequeño cambio, un gran impacto! 
    Al utilizar productos ecológicos, puedes reducir la emisión de gases de efecto invernadero 
            en un 25% y disminuir la contaminación del agua en un 40%. 
    ¡Haz la diferencia y elige productos ecológicos para un futuro más verde y saludable!
        """)
        break

    else:
        print("Opción inválida. Por favor, inténtelo de nuevo.")
    
