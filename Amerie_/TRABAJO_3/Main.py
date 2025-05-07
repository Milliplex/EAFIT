# Elaborado por:
"""
Juan José Chaparro Gutiérrez
Tomás Gutiérrez Velásquez
Amerie Sugimoto Rivera
"""

# Lista de Presupuestos
presupuestos = [0, 0, 0, 0]
regiones = ["Norteamérica", "Europa", "Latinoamérica", "Asia"]

#Libreria Para Presentacion de los Presupuestos Tipo Tabla
from tabulate import tabulate

#Libreria Para Graficar la cantidad de Productos que Hay por Categoria
import matplotlib.pyplot as plt

# Declaración de Funciones
# 1
def ingresar_presupuesto():
    for i in range(4):
        presupuestos[i] = float(input(f"Ingrese el presupuesto para {regiones[i]}: "))

# 2
def mostrar_presupuesto_inicial():
    tabla = [[regiones[i], f"${presupuestos[i]:,.2f}"] for i in range(4)]
    print(tabulate(tabla, headers=["Región", "Presupuesto"], tablefmt="grid"))

# 3
def mod_presupuesto_region():
    print("""
    Seleccione la región a modificar:
        (1) Norteamérica
        (2) Europa
        (3) Latinoamérica
        (4) Asia
    """)
    region = int(input("Ingrese la opción: "))

    if 1 <= region <= 4:
        nuevo = float(input(f"Nuevo presupuesto para {regiones[region - 1]}: "))
        presupuestos[region - 1] = nuevo  # Asignación directa del nuevo valor al presupuesto de la región
    else:
        print("Región incorrecta.")

# 4
def redistribuir_presupuesto_equi():
    total = sum(presupuestos)  # Sumar todos los presupuestos
    nuevo_presupuesto = total / 4
    presupuestos[:] = [nuevo_presupuesto] * 4  # Redistribuir el presupuesto equitativamente entre las 4 regiones
    print("Presupuesto redistribuido equitativamente.")

# 5
def simulacio_campana():
    print("Seleccione la región para la campaña:" 
          """
    (1) Norteamérica
    (2) Europa
    (3) Latinoamérica
    (4) Asia
    """)
    region = int(input("Ingrese la opción: "))
    incremento = 10000  # Aumento fijo en el presupuesto

    if 1 <= region <= 4:
        print(f"Campaña en {regiones[region - 1]}: Aumento de {incremento}")
    else:
        print("Opción incorrecta.")

# 6
def clasificar_presupuesto():
    total_presupuesto = sum(presupuestos)

    if total_presupuesto < 100000:
        print("Presupuesto Bajo")
    elif total_presupuesto <= 300000:
        print("Presupuesto Equilibrado")
    else:
        print("Presupuesto Alto")

#7
def graficar_presupuestos():
    plt.figure(figsize=(8, 5))
    # Tamaño de la Ventana emergente (donde estan las graficas)

    plt.bar(regiones, presupuestos, color='skyblue')  
    #plt.bar = grafico de barras verticales
    # regiones se toman como los valores de x (horizontal)(encabezados)
    # presupuestos valores en Vertical

    plt.title("Presupuesto por Región")  
    #Título del gráfico en la parte superior

    plt.xlabel("Región")  # Etiqueta del eje X
    plt.ylabel("Presupuesto en USD")  # Etiqueta del eje Y
    plt.show()  # Mostrar el gráfico

# Ciclo while
while True:
    print("""
                MENÚ DE OPCIONES
        (1) Ingresar presupuesto inicial
        (2) Mostrar presupuesto actual
        (3) Modificar presupuesto de una región
        (4) Redistribuir presupuesto equitativamente
        (5) Simular campaña de marketing
        (6) Clasificar presupuesto
        (7) Ver Grafica de Presupuestos
        (8) Salir
          
     Por favor, elige una opción del menú para continuar:      
          """)
    
    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        ingresar_presupuesto()
    elif opcion == 2:
        mostrar_presupuesto_inicial()
    elif opcion == 3:
        mod_presupuesto_region()
    elif opcion == 4:
        redistribuir_presupuesto_equi()
    elif opcion == 5:
        simulacio_campana()
    elif opcion == 6:
        clasificar_presupuesto()
    elif opcion == 7:
        graficar_presupuestos()
    elif opcion == 8:
        print("Saliendo del sistema...")
        break  
    else:
        print("Opción incorrecta, intente de nuevo.")
