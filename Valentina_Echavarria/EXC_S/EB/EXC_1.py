
#Lista que se le Pueden Agregar Varios Datos
lista_numeros = []

#Pedir al Usuario que Ingrese un Número como Entero
numero_usuario = int(input('Ingrese un Numero: '))

#Guardar el Número en la Lista
lista_numeros.append(numero_usuario)

#Ciclo while
desicion = input('Desea Ingresar mas Numeros? (SI/NO): ')

while desicion == 'SI':
    numero_usuario = int(input('Ingrese otro Numero: '))
    lista_numeros.append(numero_usuario)
    desicion = input('Desea Ingresar mas Numeros? (SI/NO): ')

print(f"Los numeros ingresados son: {lista_numeros}")

input('Por favor, presione un tecla para salir ')