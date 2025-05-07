
#Importar la Base de datos desde el archivo Base_Datos.py
from Base_Datos import productos_ecologicos

def actualizar_inf_pd():
    producto_actualizar = input('Ingrese el Producto cuya Información desea Actualizar: ').lower()

    # Buscar el producto en cualquier categoría y actualizar su descripción
    for categoria in productos_ecologicos.values():
        if producto_actualizar in categoria:
            nueva_descripcion = input("Ingrese la nueva Descripción para el Producto: ")
            categoria[producto_actualizar]['descripcion'] = nueva_descripcion
            print(f"La información del producto {producto_actualizar.title()} ha sido actualizada con éxito.")
            return  # Salir de la función después de actualizar el producto

    # Si el producto no se encuentra
    print("Producto no encontrado. No se puede actualizar la información.")
