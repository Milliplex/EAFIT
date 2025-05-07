
#Importar la Base de datos desde el archivo Base_Datos.py
from Base_Datos import productos_ecologicos

def buscar_pd_ia():
    buscador = input('Ingrese el Producto a Buscar: ').lower()
    encontrado = False  # Inicializar variable

    for productos in productos_ecologicos.items():
        for producto, datos in productos.items():
            if producto == buscador:
                impacto = datos.get('impacto', 'No especificado').capitalize()
                print(f"El producto '{producto.title()}' es de: {impacto} Impacto Ambiental")
                encontrado = True
                break
        if encontrado:
            break

    if not encontrado:
        print('No se encontró la información.')

