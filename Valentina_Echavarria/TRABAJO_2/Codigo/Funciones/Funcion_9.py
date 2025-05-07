# Importar la base de datos
from Base_Datos import productos_ecologicos

def cargar_productos_desde_archivo(ruta_archivo):
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                linea = linea.strip()

                # Ignorar líneas que son comentarios (empiezan con /// o //)
                if linea.startswith("//") or not linea:
                    continue

                # Separar usando comas
                partes = linea.split(',')

                # Verificar que tenga 4 partes
                if len(partes) != 4:
                    print("Línea con formato incorrecto:", linea)
                    continue

                # Quitar espacios alrededor de cada parte
                nombre = partes[0].strip().lower()
                descripcion = partes[1].strip()
                impacto = partes[2].strip().lower()
                categoria = partes[3].strip().lower()

                # Verificar que la categoría exista
                if categoria in productos_ecologicos:
                    productos_ecologicos[categoria][nombre] = {
                        'descripcion': descripcion,
                        'impacto': impacto
                    }
                    print(f"Producto agregado: {nombre.title()}")
                else:
                    print(f"Categoría inválida: {categoria}")
    except FileNotFoundError:
        print("No se encontró el archivo:", ruta_archivo)
