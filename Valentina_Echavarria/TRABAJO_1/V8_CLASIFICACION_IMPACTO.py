
#Creacion de las Listas Basicas

productos = []
categorias = []
detalles_produc = []

#Agregar productos a una Categoria Especiica
alimentos_orga = ["Uva"]
productos_hc = []
alterna_sos = []
productos_limE = []

#+V6 se necesito agregar nuevas listas para poder modificar los detalles
deta_alimentos_orga = []
deta_productos_hc = []
deta_alterna_sos = []
deta_productos_limE = []

#Base de Datos 

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
    (5) Modificar Detalles de un Producto N/A
    (6) Ver Productos Ecologicos
    (7) Clasificacion Segun Impacto Ambiental
    (8) Salir del Programa
    """)

    opcion = int(input('Ingrese la Opcion: '))

    # Pedir Datos de las Listas
    if opcion == 1:
        an_productos = input('Ingrese el Nombre del Producto: ').strip().lower()
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
            deta_alimentos_orga.append(dt_productos)

        elif an_categoria == 2:
            an_categoria = 'Productos de Higiene y Cosmetica'
            categorias.append(an_categoria)
            productos_hc.append(an_productos)
            deta_productos_hc.append(dt_productos)

        elif an_categoria == 3:
            an_categoria = 'Alternativas Sostenibles'
            categorias.append(an_categoria)
            alterna_sos.append(an_productos)
            deta_alterna_sos.append(dt_productos)

        elif an_categoria == 4:
            an_categoria = 'Productos de Limpieza Ecologicos'
            categorias.append(an_categoria)
            productos_limE.append(an_productos)
            deta_productos_limE.append(dt_productos)

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
            print(F"Los Productos Organicos son: {alimentos_orga}, y los detalles son: {deta_alimentos_orga} (respectivamente)")
        elif buscador == 2:
            print(F"Los Productos de Higiene y Cosmetica son: {productos_hc}, y los detalles son: {deta_productos_hc} (respectivamente)")
        elif buscador == 3:
            print(F"Los Productos Alternativas Sostenibles son: {alterna_sos}, y los detalles son: {deta_alterna_sos} (respectivamente)")
        elif buscador == 4:
            print(F"Los Productos de Limpieza Ecologicos son: {productos_limE}, y los detalles son: {deta_productos_limE} (respectivamente)")
        else:
            print('Categoria No Valida')

    
    # Verificar Existencias
    elif opcion == 3:
        buscador = input('Ingrese el Producto a Buscar: ').strip().lower()
        if buscador in productos:
            posicion = productos.index(buscador)
            print('El Producto si existe')
        else:
            print("Producto no encontrado")

    # Borrar Producto Especifico de la Base de datos
    elif opcion == 4:
        buscador = input('Ingrese el Producto a Eliminar: ').strip().lower()
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

    # Ver Todos Los Productos Ecologicos
    elif opcion == 6:
        print('Los Productos Organicos son: ', alimentos_orga)
        print('Los Productos de Higiene y Cosmetica son: ', productos_hc)
        print('Las Alternativas Sostenibles son: ', alterna_sos)
        print('Los Productos de Limpieza Ecologicos son: ', productos_limE)

    # Buscar Productos y saber su Impacto Ambiental
    elif opcion == 7:
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
    elif opcion == 8:
        print("""
        ¡Un pequeño cambio, un gran impacto! 
        Al utilizar productos ecológicos, puedes reducir la emisión de gases de efecto invernadero en un 25% y disminuir la contaminación del agua en un 40%. 
        ¡Haz la diferencia y elige productos ecológicos para un futuro más verde y saludable!
        """)
        break
    else:
        print("Opción inválida. Por favor, inténtelo de nuevo.")
