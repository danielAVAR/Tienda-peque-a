import agregar 

agregar_producto = agregar

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
    

while True:
    menu_main()
    opc = int(input("Seleccione una Opcion"))
    if opc == 1:
        agregar_producto
    elif opc == 2:
        pass
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

