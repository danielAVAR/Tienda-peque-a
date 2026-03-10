def menu_main():
    print("""
================================
===== SISTEMA DE INVENTARIO ====
1. Agregar producto
2. Listar Producto
3. Actualizar Producto
4. Eliminar
5. Calcular Valor Total del Inventario
6. Salir
=================================
=================================
""")

def agregar_producto(productos):
    nombre = input( "Nombre del Producto: ")
    precio = input ("Precio del Producto: Q")
    cantidad = int(input("Cantidad del producto: "))

    data_producto = {
        "Precio": precio,
        "Cantidad": cantidad
        }
    
    productos[nombre] = data_producto


    return productos

def listar_productos (productos):
    if not productos:
        print("No hay productos en el inventario")
    else:
        print("Productos en el inventario: \n")
        for nombre, data in productos.items():
            print(f"Nombre: {nombre} \n Precio: Q{data['Precio']} \n Cantidad: {data['Cantidad']} \n")




productos = {}

while True:
    menu_main()
    opc = int(input("Seleccione una Opcion: "))
    if opc == 1:
        agregar_producto(productos)
    elif opc == 2:
        listar_productos(productos)
    elif opc == 3:
        pass
    elif opc == 4:
        pass
    elif opc == 5:
        pass
    elif opc == 6:
        print("Bye lol")
        break
    else:
        print("Opcion Invalida")
        pass

