# Proyecto de Gestión de Presupuesto de Marketing

# Elaborado por:
"""
Juan José Chaparro Gutiérrez
Tomás Gutiérrez Velásquez
Amerie Sugimoto Rivera
"""

from tabulate import tabulate
import matplotlib.pyplot as plt

# Lista de presupuestos y nombres de regiones
presupuestos = [0, 0, 0, 0]
regiones = ["Norteamérica", "Europa", "Latinoamérica", "Asia"]

# 1. Ingresar presupuesto inicial
def ingresar_presupuesto():
    for r in range(4):
        print("Ingrese el presupuesto para", regiones[r])
        valor = float(input())
        if valor < 0 or valor > 1000000:
            print("Presupuesto inválido. Debe estar entre 0 y 1,000,000.")
            return
        presupuestos[r] = valor

# 2. Mostrar presupuestos actuales (con tabulate)
def mostrar_presupuesto_inicial():
    tabla = []
    for r in range(4):
        tabla.append([regiones[r], presupuestos[r]])
    print(tabulate(tabla, headers=["Región", "Presupuesto"], tablefmt="grid"))

# 3. Modificar presupuesto de una región (con control de tope)
def mod_presupuesto_region():
    print("""
    Seleccione la Region a Modificar
        1. Norteamérica
        2. Europa
        3. Latinoamérica
        4. Asia
          """)
    opcion = int(input("Ingrese la opción: "))

    if 1 <= opcion <= 4:
        print("Ingrese el nuevo presupuesto para " + regiones[opcion - 1] + ":")
        nuevo = float(input())
        if nuevo < 0 or nuevo > 1000000:
            print("Presupuesto inválido. Debe estar entre 0 y 1,000,000.")
        else:
            presupuestos[opcion - 1] = nuevo
    else:
        print("Opción inválida.")

# 4. Redistribuir presupuesto equitativamente
def redistribuir_presupuesto_equi():
    suma = sum(presupuestos)
    nuevo = suma / 4
    for r in range(4):
        presupuestos[r] = nuevo
    print("Presupuesto redistribuido en partes iguales.")

# 5. Simular campaña con tope máximo
def simulacion_campana():
    print("""
    Seleccione la Region a Realizar la Simulacion
        1. Norteamérica
        2. Europa
        3. Latinoamérica
        4. Asia
          """)
    region = int(input("Ingrese la opción: "))
    aumento = 10000

    if region >= 1 and region <= 4:
        nueva = presupuestos[region - 1] + aumento
        suma_total = 0
        for r in range(4):
            if r == region - 1:
                suma_total += nueva
            else:
                suma_total += presupuestos[r]

        if suma_total > 100000:
            print("No se puede aumentar. Se pasa del tope máximo.")
        else:
            presupuestos[region - 1] = nueva
            print("Se aumentó el presupuesto de", regiones[region - 1])
    else:
        print("Opción inválida.")

# 6. Clasificar presupuesto total
def clasificar_presupuesto():
    suma = sum(presupuestos)

    if suma < 100000:
        print("Presupuesto Bajo")
    elif suma <= 300000:
        print("Presupuesto Equilibrado")
    else:
        print("Presupuesto Alto")

# 7. Cargar presupuestos desde archivo
def cargar_desde_archivo():
    try:
        archivo = open("datos.txt", "r")
        datos = archivo.read().split(",")
        for i in range(4):
            presupuestos[i] = float(datos[i])
        archivo.close()
        print("Presupuestos cargados desde archivo.")
    except:
        print("Error al leer el archivo. Asegúrese de que 'datos.txt' exista y tenga 4 valores separados por coma.")

# 8. Graficar presupuestos con Matplotlib
def graficar_presupuestos():
    plt.bar(regiones, presupuestos, color='lightblue')
    plt.title("Presupuesto por Región")
    plt.xlabel("Regiones")
    plt.ylabel("Presupuesto")
    for i in range(len(presupuestos)):
        plt.text(i, presupuestos[i], str(presupuestos[i]))
    plt.tight_layout()
    plt.show()


#SUSTENTACION

#1
#Nueva Funcion que Triplique el Valor de una Categoria Especifica
def multiplicar_presupuesto():
    print("""
    Seleccione la Region a Modificar
        1. Norteamérica
        2. Europa
        3. Latinoamérica
        4. Asia
          """)
    opcion = int(input("Ingrese la opción: "))

    if opcion >= 1 and opcion <= 4:
       presupuestos[opcion - 1] *= 3

       print("El Presupuesto para la Region ha sido multiplicada") 

    else:
        print('Opcion no Valida. Verifique la Opcion Ingresada ')

#2
#Reiniciar Datos y dejar todos los Presupuestos en 0
def reiniciar_presupuestos():
    reinicar = input("¿Está seguro de que desea reiniciar los presupuestos? (si/no): ").lower()
    while reinicar == "si":
        global presupuestos #Toma todos los Valores de La lista (los presupuestos)
        presupuestos = [0, 0, 0, 0] #Actualiza los valores (presupuestos) a 0
        print("Los presupuestos han sido reiniciados a 0.")

        break

#3
""""
1) Se le pide al usuario que ingrese el numero correspondiente
en base a la tabla, la region que desea modificar
2) Ese ingrese se guara en una variable llamada opcion
3) Se verifica que la opcion(region) ingresada sea valida
4) Si la opcion es valida, se le pide al usuario que ingrese el nuevo presupuesto
5) Se verifica que el nuevo presupuesto sea valido (topes)
6) Si el nuevo presupuesto es valido, se actualiza el presupuesto de la region seleccionada
7) Si la opcion no es valida, se imprime un mensaje de error
"""

#4
#Que tipo de variable es la linea XX?????

#5
#Ciclos While
""""
While
1) -Reiniciar Datos y dejar todos los Presupuestos en 0
    1. Se usa para reinicar los presupuestos solo si el usuario lo desea
    esto mediante a un input en cual se le pregunta al usuario si desea reiniciar los presupuestos
    2. Si el usuario ingresa "si", se reinician los presupuestos a 0
    3. Si el usuario ingresa "no", se sale del ciclo 
    4. Vuelve al Menu Principal

2) -Menu Principal
    1. Se usa para mostrar el menu de opciones al usuario mientras el programa se ejecute
    2. Se usa un ciclo while para que el menu se muestre continuamente hasta que el usuario decida salir
    3. Se usa un input para que el usuario ingrese la opcion deseada
    4. Mientras la opcion sea difetente a 9 que es el Break del Ciclo, este se seguira ejecutando 
"""

#6
#Condiciones 
"""
Estructura Basica de un If, Elif y Else

If: se usa para verificar si una condicion es verdadera
    1) Si la condicion es verdadera, se ejecuta el bloque de codigo dentro del if
    2) Si la condicion es falsa, se pasa al siguiente bloque de codigo

Elif: se usa para verificar si una segunda condicion es verdadera
    1) Si la condicion es verdadera, se ejecuta el bloque de codigo dentro del elif
    2) Si la condicion es falsa, se pasa al siguiente bloque de codigo

Else: se usa para ejecutar un bloque de codigo si ninguna de las condiciones anteriores son verdaderas
    1) Se ejecuta el bloque de codigo dentro del else
"""

#7
#Nueva Funcion que divide en 3 los presupuestos de las regiones 
def dividir_presupuesto():
    dividir = input("¿Está seguro de que desea dividir cada Presupuesto en 3? (si/no): ").lower()
    while dividir == "si":
        for i in range(len(presupuestos)):
            presupuestos[i] /= 3
        print("Los presupuestos han sido divididos en 3.")

        break

#8
#Opcion que se llame "saludo" y que muestra un mensaje de saludo al usuario
def saludo():
    print("¡Hola! Bienvenido al sistema de gestión de presupuestos de marketing.")

#9
#Nueva Funcion que reduce a la mitad el presupuesto de una region en 2
def reducir_presupuesto():
    print("""
    Seleccione la Region a Modificar
        1. Norteamérica
        2. Europa
        3. Latinoamérica
        4. Asia
          """)
    opcion = int(input("Ingrese la opción: "))

    if opcion >= 1 and opcion <= 4:
       presupuestos[opcion - 1] /= 2

       print("El Presupuesto para la Region ha sido reducido a la mitad") 

    else:
        print('Opcion no Valida. Verifique la Opcion Ingresada ')

#10 
#Grafica los presupuestos de cada region
#Ya existe en el programa, opcion 8


# Menú principal
while True:
    print("""
          
------------------MENU DE OPCIONES----------------
    1. Ingresar presupuesto inicial
    2. Mostrar presupuesto actual
    3. Modificar presupuesto de una región
    4. Redistribuir presupuesto equitativamente
    5. Simular campaña de marketing
    6. Clasificar presupuesto
    7. Cargar presupuestos desde archivo
    8. Graficar presupuestos
    9. Salir
          
    10. Sustentacion #1 Triplicar Presupuesto
    11. Sustentacion #2 Reiniciar Presupuestos
    12. Sustentacion #3 Dividir Presupuesto 
    13. Sustentacion #4 Saludo
    14. Sustentacion #5 Reducir Presupuestos en 2
--------------------------------------------------    
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
        simulacion_campana()
    elif opcion == 6:
        clasificar_presupuesto()
    elif opcion == 7:
        cargar_desde_archivo()
    elif opcion == 8:
        graficar_presupuestos()

    elif opcion == 10:
        multiplicar_presupuesto()
    elif opcion == 11:
        reiniciar_presupuestos()
    elif opcion == 12:
        dividir_presupuesto()
    elif opcion == 13:
        saludo()
    elif opcion == 14:
        reducir_presupuesto()


    elif opcion == 9:
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida.")