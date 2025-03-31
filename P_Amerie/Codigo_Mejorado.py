# Elaborado por:

"""
Juan José Chaparro Gutiérrez
Tomás Gutiérrez Velásquez
Amerie Sugimoto Rivera
"""

# Declaración de variables individuales
presupuesto_norteamerica = 0
presupuesto_europa = 0
presupuesto_latinoamerica = 0
presupuesto_asia = 0
opcion = 0

# Ciclo while
while True:

    print ("Menú de Opciones:"
        """
              
    (1) Ingresar presupuesto inicial
    (2) Mostrar presupuesto actual
    (3) Modificar presupuesto de una región
    (4) Redistribuir presupuesto equitativamente
    (5) Simular campaña de marketing
    (6) Clasificar presupuesto
    (7) Salir
        """)
    opcion = int(input("Ingrese una opción: "))

    # Condicional para ejecutar la opción seleccionada
    if opcion == 1:
        presupuesto_norteamerica = float(input("Ingrese el presupuesto para Norteamérica: "))
        presupuesto_europa = float(input("Ingrese el presupuesto para Europa: "))
        presupuesto_latinoamerica = float(input("Ingrese el presupuesto para Latinoamérica: "))
        presupuesto_asia = float(input("Ingrese el presupuesto para Asia: "))

    elif opcion == 2:
        print("Presupuesto Norteamérica:", presupuesto_norteamerica)
        print("Presupuesto Europa:", presupuesto_europa)
        print("Presupuesto Latinoamérica:", presupuesto_latinoamerica)
        print("Presupuesto Asia:", presupuesto_asia)

    elif opcion == 3:
        print ("Seleccione la región a modificar:"
        """
              
    (1) Norteamérica
    (2) Europa
    (3) Latinoamérica
    (4) Asia
        """)

        region = int(input("Ingrese la opción: "))

        if region == 1:
            presupuesto_norteamerica = float(input("Nuevo presupuesto para Norteamérica: "))
        elif region == 2:
            presupuesto_europa = float(input("Nuevo presupuesto para Europa: "))
        elif region == 3:
            presupuesto_latinoamerica = float(input("Nuevo presupuesto para Latinoamérica: "))
        elif region == 4:
            presupuesto_asia = float(input("Nuevo presupuesto para Asia: "))
        else:
            print("Región incorrecta.")

    elif opcion == 4:
        total = presupuesto_norteamerica + presupuesto_europa + presupuesto_latinoamerica + presupuesto_asia
        presupuesto_norteamerica = total / 4
        presupuesto_europa = total / 4
        presupuesto_latinoamerica = total / 4
        presupuesto_asia = total / 4
        print("Presupuesto redistribuido equitativamente.")

    elif opcion == 5:
        # Simulación de una campaña de marketing
        print ("Seleccione la región para la campaña:"
                """
                    
        (1) Norteamérica
        (2) Europa
        (3) Latinoamérica
        (4) Asia
                """)
        region = int(input("Ingrese la opción: "))
        incremento = 10000  # Aumento fijo en el presupuesto

        if region == 1:
            print("Campaña en Norteamérica: Aumento de", incremento)
        elif region == 2:
            print("Campaña en Europa: Aumento de", incremento)
        elif region == 3:
            print("Campaña en Latinoamérica: Aumento de", incremento)
        elif region == 4:
            print("Campaña en Asia: Aumento de", incremento)
        else:
            print("Opción incorrecta.")

    elif opcion == 6:
        # Clasificación del presupuesto total
        total_presupuesto = presupuesto_norteamerica + presupuesto_europa + presupuesto_latinoamerica + presupuesto_asia
        if total_presupuesto < 100000:
            print("Presupuesto Bajo")
        elif total_presupuesto <= 300000:
            print("Presupuesto Equilibrado")
        else:
            print("Presupuesto Alto")

    elif opcion == 7:
        print("Saliendo del sistema...")
        break  # Finaliza el programa

    else:
        print("Opción incorrecta, intente de nuevo.")
