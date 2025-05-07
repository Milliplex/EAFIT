
#Importar la Base de datos desde el archivo Base_Datos.py
from Base_Datos import productos_ecologicos

#Definicion de Funciones
#1
def anadir_pd():   
    nuevo_producto = input('Ingrese el Nombre del Producto: ').lower()

    # Verificar si el producto ya existe en alguna categoría
    if any(nuevo_producto in categoria for categoria in productos_ecologicos.values()):
        print("El producto ya existe en el sistema. No se puede volver a agregar.")
        
    else:
        descripcion_producto = input('Ingrese la Descripción del Producto: ')

        # Seleccionar el impacto ambiental con un micro menú
        impacto_producto = int(input("""Ingrese el Impacto Ambiental del Producto
        (1) Alto
        (2) Medio
        (3) Bajo
        (4) No Especificado
            """))
        if impacto_producto == 1:
            impacto = "alto"
        elif impacto_producto == 2:
            impacto = "medio"
        elif impacto_producto == 3:
            impacto = "bajo"
        elif impacto_producto == 4:
            impacto = "no especificado"
        else:
            print("Impacto no válido.")
            
        # Seleccionar la categoría con un micro menú
        agregar_categoria = int(input('Ingrese el Número de la Categoría a la que Pertenece el Producto: ' 
        """
        (1) Alimentos Orgánicos
        (2) Productos de Higiene y Cosmética
        (3) Alternativas Sostenibles
        (4) Productos de Limpieza Ecológicos
        (5) N/A
            """))

        if agregar_categoria == 1:
            productos_ecologicos['alimentos organicos'][nuevo_producto] = {'descripcion': descripcion_producto, 'impacto': impacto}
            print(f'El producto {nuevo_producto.title()} ha sido agregado a la categoría de Alimentos Orgánicos.')

        elif agregar_categoria == 2:
            productos_ecologicos['higiene cosmetica'][nuevo_producto] = {'descripcion': descripcion_producto, 'impacto': impacto}
            print(f'El producto {nuevo_producto.title()} ha sido agregado a la categoría de Higiene y Cosmética.')

        elif agregar_categoria == 3:
            productos_ecologicos['alternativas sostenibles'][nuevo_producto] = {'descripcion': descripcion_producto, 'impacto': impacto}
            print(f'El producto {nuevo_producto.title()} ha sido agregado a la categoría de Alternativas Sostenibles.')

        elif agregar_categoria == 4:
            productos_ecologicos['limpieza ecologica'][nuevo_producto] = {'descripcion': descripcion_producto, 'impacto': impacto}
            print(f'El producto {nuevo_producto.title()} ha sido agregado a la categoría de Limpieza Ecológica.')

        elif agregar_categoria == 5:
            categoria = "no especificada"
            productos_ecologicos['no especificada'][nuevo_producto] = {'descripcion': descripcion_producto, 'impacto': impacto}
            print(f'El producto {nuevo_producto.title()} ha sido agregado a la categoría "No especificada".')

        else:
            print('Categoría no válida.')
          