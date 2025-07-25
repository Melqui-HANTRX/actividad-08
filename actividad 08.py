producto = []

while True:
    print("\n---MENU DE TIENDA---")
    print("1. Agregar producto. ")
    print("2. Modificar un producto. ")
    print("3. Eliminar un producto. ")
    print("4. Ver los productos. ")
    print("5. Salir del programa. ")

    menu_de_opciones = input("Eliga una opcion (1-5): ")

    match menu_de_opciones:
        case "1":
            tienda = input("Agrege un producto a su canasta: ")
            producto.append(tienda)
            print("Elemento guardado en su canasta.")
        case "2":
            print("Lista actual", producto)
            valor_de_tienda = int(input("Ingrese el indice del elemento o el nombre, el indice comienza de (0): "))
            nuevo_valor = input("Ingrese el nuevo producto: ")
            producto[valor_de_tienda] = nuevo_valor
            print("Producto modificado.")
        case "3":
            print("lista actual: ", producto)
            valor = input("Ingrese el producto a eliminar (puede ser por indice o nombre): ")
            producto.remove(valor)
            print("El producto fue eliminado. ")
        case "4":
            print("Productos en su canasta actuales: ", producto)
        case "5":
            print("Saliendo del programa.....")
            break
        case _:
            print("Opción invalida, intente de nuevo. ")