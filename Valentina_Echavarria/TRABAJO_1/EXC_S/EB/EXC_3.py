
#Inventario Inicial
inventario = {
    "CocaCola": 10,
    "Fanta": 15,
    "Sprite": 20,
    "Agua": 5
    }

#Mostar Inventario
def mostrar_inventario(inventario):
    print("Inventario Actual:")
    for producto, cantidad in inventario.items():
        print(f"{producto}: {cantidad} unidades")

#Llamar a la funcion
mostrar_inventario(inventario)

#Vender Producto
def vender_producto(inventario):
    producto = input("Ingrese el producto a vender: ").lower
    cantidad = int(input(f"Cuantas unidades {producto} quiere vender? "))

    if producto in inventario:
        if inventario[producto] >= cantidad:
            inventario[producto] -= cantidad
            print(f"Se vendieron {cantidad} unidades de {producto}")
        else:
            print(f"No hay suficientes unidades de {producto} para vender")
    else:
        print(f"No tenemos {producto} en inventario")

vender_producto(inventario)






