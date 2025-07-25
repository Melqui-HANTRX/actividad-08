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
            valor_de_tienda =
