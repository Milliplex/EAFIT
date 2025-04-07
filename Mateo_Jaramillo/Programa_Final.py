opcion_menu = int(input('Ingrese la Opcion del Menu: '))

if opcion_menu == 1:   
    asignaturas_repro_1 = int(input('Ingrese la cantidad de Asignaturas Reprobadas (0-3): '))
    asistencia_clase_1 = int(input('Ingrese la Frecuencia de Asistencia a Clases (0-5): '))
    recursos_acad_1 = int(input('Ingrese la cantidad de uso de Recursos Academicos (0-5): '))

    if asignaturas_repro_1 <= 3 and  asistencia_clase_1 <= 5 and recursos_acad_1 <= 5:
            print('La Cantidad de Asginaturas Reprobadas es:', asignaturas_repro_1)
            print('La Frecuencia de Asistencia a Clases es:', asistencia_clase_1)
            print('La Cantidad de usos de Recursos Academicos fue de:', recursos_acad_1)
    else: print('Error: Revise los datos ingresados')
    
elif opcion_menu in [2, 3, 4]:
    asignaturas_repro_2 = int(input('Ingrese la cantidad de Asignaturas Reprobadas (0-3): '))
    asistencia_clase_2 = int(input('Ingrese la Frecuencia de Asistencia a Clases (0-5): '))
    recursos_acad_2 = int(input('Ingrese la cantidad de uso de Recursos Academicos (0-5): '))

    if asignaturas_repro_2 <= 1 and asistencia_clase_2 <=5 and recursos_acad_2 <= 5:
                print('Riesgo bajo')
    elif asignaturas_repro_2 <= 2 and asistencia_clase_2 <=5 and recursos_acad_2 <= 5:
                    print('Riesgo moderado')
    elif asignaturas_repro_2 <= 3 and asistencia_clase_2 <=5 and recursos_acad_2 <= 5:
                        print('Riesgo Alto')
    else: print('Error: Revise los datos ingresados')           
else: 
    print('Error: Opcion de Menu Invalido')