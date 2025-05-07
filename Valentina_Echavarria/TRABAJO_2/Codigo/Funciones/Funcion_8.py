
#Importar la Base de datos desde el archivo Base_Datos.py
from Base_Datos import productos_ecologicos

#Libreria Para Graficar la cantidad de Productos que Hay por Categoria
import matplotlib.pyplot as plt

def graficar_cantidad():
    # Extraer categorías y contar la cantidad de productos en cada una
    categorias = []
    cantidades = []

    for categoria, productos in productos_ecologicos.items():
        categorias.append(categoria.title())  # Capitaliza los nombres de las categorías
        cantidades.append(len(productos))     # Cuenta los productos en cada categoría

    # Crear gráfica de barras
    plt.figure(figsize=(10, 6))
    # Crea la Ventana de la Gráfica
    # Define tamaño en pulgadas de las gráficas

    plt.bar(categorias, cantidades, color=['green', 'pink', 'orange', 'blue', 'gray'])
    # Barras Verticales en el eje x

    plt.title('Cantidad de Productos por Categoría')
    # Título de la Gráfica

    plt.xlabel('Categorías')
    plt.ylabel('Cantidad de Productos')
    # Coloca las Etiquetas/Nombres de los ejes

    plt.tight_layout()
    # Ajusta los espacios entre las barras de las gráficas

    plt.show()
    # Muestra la Gráfica en la pantalla = print
