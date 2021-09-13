import producto

# Variables generales

# Variables glbales
MENU = (
    (1, "AGREGAR UN PRODUCTO"),
    (2, "ELIMINAR UN PRODUCTO"),
    (3, "EDITAR UN PRODUCTO"),
    (4, "IMPORTAR DESDE JSON"),
    (5, "EXPORTAR A JSON"),
    (6, "SALIR"),
)

def imprimir_menu():
    """ Imprime el menú de la aplicación y lee la respuesta del
    usuario.
    """
    print()
    print("-" * 60)
    for i, texto in MENU:  # opcion = (0, "Salir")
        print(f"{i}. {texto}")
    print("-" * 60)
    respuesta_str = input("Elige una opción: ")
    try:
        respuesta = int(respuesta_str)
    except ValueError:
        respuesta = -1

    return respuesta


def main():
    """ función principal del programa """
    productos = []  # Lista de productos de tipo Producto
    continuar = True
    while continuar:
        producto.imprimir_productos(productos)
        opcion = imprimir_menu()
        if opcion == 1:  # Adicionar un producto
            producto.agrega_producto(productos)
        elif opcion == 2:  # Eliminar un producto
            producto.elimina_producto(productos)
        elif opcion == 3:  # Editar un producto
            pass
        elif opcion == 4:  # Importar de JSON
            productos = producto.importar_de_json()
        elif opcion == 5:  # Exportar a JSON
            producto.exportar_a_json(productos)
        elif opcion == 6:  # Salir de programa
            continuar = False
            print("Saliste del programa")
        else:
            print("La opcion no existe, intenta con otra opcion")

if __name__ == '__main__':
    main()