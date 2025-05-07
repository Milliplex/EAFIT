
#Importar la Base de datos desde el archivo Base_Datos.py
from Base_Datos import productos_ecologicos

def verificar_existencia():   
    producto_a_buscar = input('Ingrese el Nombre del Producto a Buscar: ').lower()

    # Verificar si el producto ya existe en alguna categoría
    if any(producto_a_buscar in categoria for categoria in productos_ecologicos.values()):
        print(f"El Producto {producto_a_buscar.title()} ya existe en el Sistema")
    else:
        print(f"El Producto {producto_a_buscar.title()} no existe en el Sistema")