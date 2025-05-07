
#Importar la Base de datos desde el archivo Base_Datos.py
from Base_Datos import productos_ecologicos

def eliminar_pd():
    producto_eliminar = input('Ingrese el Producto a Eliminar: ').lower()

    # Buscar y eliminar el producto de cualquier categoría
    for categoria in productos_ecologicos.values():
        if producto_eliminar in categoria:
            categoria.pop(producto_eliminar)
            print(f"El Producto {producto_eliminar.title()} ha sido eliminado con éxito")
            return  # Salir de la función una vez que el producto es eliminado

    # Si el producto no se encuentra
    print("Producto no encontrado")
