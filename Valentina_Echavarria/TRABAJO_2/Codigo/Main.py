
            #Definicion de Funciones

#1 ESTUDIAR (Diccionario y Any)
from Funciones.Funcion_1 import anadir_pd   

#2 ESTUDIAR (Any)
from Funciones.Funcion_2 import buscar_pd_cat

#3
from Funciones.Funcion_3 import verificar_existencia

#4 ESTUDIAR (For)
from Funciones.Funcion_4 import eliminar_pd

#5 ESTUDIAR (.value)
from Funciones.Funcion_5 import actualizar_inf_pd

#6
from Funciones.Funcion_6 import ver_pd_ec

#7 ESTUDIAR (.get)
from Funciones.Funcion_7 import buscar_pd_ia

#8 ESTUDIAR 
from Funciones.Funcion_8 import graficar_cantidad

#9 Añadir de Productos Mediante archivos .txt
from Funciones.Funcion_9 import cargar_productos_desde_archivo

#---.---.---.---.---.---.#
print("""
                          ¡Hola Bienvenido!
    Este programa ha sido diseñado para ayudarte a conocer, gestionar y 
consultar una base de datos de productos ecológicos clasificados por 
                categoría y su impacto ambiental
""")

while True:
    print("""
--------------------------- MENÚ ---------------------------
    (1) Añadir Productos a la Base de Datos
    (2) Buscar Productos por Categoria
    (3) Busqueda de un Producto en la Base de Datos 
    (4) Eliminar un Producto de la Base de Datos
    (5) Actualizar Informacion de un Producto
    (6) Ver Todos los Productos Ecologicos
    (7) Buscar Productos y Saber Cual es su Impacto Ambiental  
    (8) Ver Grafica de Cantidad de Productos por Categoria  
    (9) Agregar o Modificar Productos Mediante archivo 'prodcutos.txt'
    (10) Salir del Programa
          
    Por favor, elige una opción del menú para continuar:
---------------------------- . ---------------------------- """)

    opcion = int(input('Ingrese la Opcion: '))

    # Añadir Productos a Listas
    if opcion == 1:
        anadir_pd()

    # Buscar Productos por Categoria
    elif opcion == 2:
        buscar_pd_cat()
 
    # Verificar Existencias
    elif opcion == 3:
        verificar_existencia()

    # Borrar Producto Especifico de la Base de datos
    elif opcion == 4:
        eliminar_pd()

    #Actualizar Informacion de un Producto
    elif opcion == 5:
        actualizar_inf_pd()

    # Ver Todos Los Productos Ecologicos
    elif opcion == 6:
        ver_pd_ec()

    # Buscar Productos y saber su Impacto Ambiental
    elif opcion == 7:
        buscar_pd_ia()

    #Ver Grafica de Cantidad de Productos por Categoria
    elif opcion == 8:
        graficar_cantidad()

    #Añadir Productos Mediante un archivo .txt
    elif opcion == 9:
        cargar_productos_desde_archivo("Codigo/productos.txt")

    # Salir
    elif opcion == 10:
        print("""
                        ¡Gracias por utilizar el Programa!
              
                        ¡Un pequeño cambio, un gran impacto! 
    Al utilizar productos ecológicos, puedes reducir la emisión de gases de efecto invernadero 
            en un 25% y disminuir la contaminación del agua en un 40%. 
    ¡Haz la diferencia y elige productos ecológicos para un futuro más verde y saludable!
              
saliendo del sistema...
        """)
        break

    else:
        print("Opción inválida. Por favor, inténtelo de nuevo.")
#---.---.---.---.---.---.#