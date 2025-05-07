
#Importar la Base de datos desde el archivo Base_Datos.py
from Base_Datos import productos_ecologicos

#Libreria Para Presentacion de los Productos Tipo Tabla
from tabulate import tabulate


#2 ESTUDIAR
def buscar_pd_cat():
    buscador = int(input('¿Qué productos de qué categoría desea visualizar?: '
                         """

    (1) Alimentos Orgánicos
    (2) Productos de Higiene y Cosmética 
    (3) Alternativas Sostenibles
    (4) Productos de Limpieza Ecológicos
    (5) No Especificada
        """))

    if buscador == 1:
        categoria = 'alimentos organicos'
    elif buscador == 2:
        categoria = 'higiene cosmetica'
    elif buscador == 3:
        categoria = 'alternativas sostenibles'
    elif buscador == 4:
        categoria = 'limpieza ecologica'
    elif buscador == 5:
        categoria = 'no especificada'
    else:
        print('Categoría no válida.')
        

    # Obtener productos de la categoría seleccionada
    productos = productos_ecologicos.get(categoria, {})
    if productos:
        print(f"\n--- {categoria.title()} ---")
        tabla = [[producto.title(), datos['descripcion']] for producto, datos in productos.items()]
        print(tabulate(tabla, headers=["Producto", "Descripción"], tablefmt="fancy_grid"))
    else:
        print(f"No hay productos registrados en la categoría '{categoria.title()}'.")

