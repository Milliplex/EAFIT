
#Importar la Base de datos desde el archivo Base_Datos.py
from Base_Datos import productos_ecologicos

#Libreria Para Presentacion de los Productos Tipo Tabla
from tabulate import tabulate

def ver_pd_ec():
    # Recorre todas las categorías en el diccionario
    for categoria, productos in productos_ecologicos.items():
        print(f"\n--- {categoria.title()} ---")
        
        # Crea la tabla de productos para cada categoría
        tabla = [[producto.title(), datos['descripcion']] for producto, datos in productos.items()]
        
        # Muestra la tabla con tabulate
        print(tabulate(tabla, headers=["Producto", "Descripción"], tablefmt="fancy_grid"))
