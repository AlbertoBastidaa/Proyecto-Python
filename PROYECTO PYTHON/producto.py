import json

NOMBRE_JSON = "productos.json"


class Producto():
    def __init__(self, id_, nombre, talla, cantidad, precio):
        """ constructor de la clase """
        self.id = id_
        self.nombre = nombre
        self.talla = talla
        self.cantidad = cantidad
        self.precio = precio

    @property
    def subtotal(self):
        """ Calcula el subtotal en tiempo real """
        return self.cantidad * self.precio
    
    def __str__(self):
        return f"({self.id}) {self.nombre}"

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "talla" : self.talla,
            "cantidad": self.cantidad,
            "precio": self.precio,
        }


def imprimir_productos(productos):
    print()
    print("Lista de productos")
    print("-" * 20)
    for p in productos:
        print(p)
    print("-" * 20)

def agrega_producto(productos):
    print()
    id_ = int(input("Digita el id del articulo: "))
    nombre = input("Digita el nombre del articulo: ")
    talla = input("¿Cual es la talla? (chica, mediana, grande o NA): ")
    cantidad = int(input(f"¿Cuantos {nombre} se tienen?: "))
    precio = float(input(f"¿Cuanto vale el/la {nombre}?: "))

    producto = Producto(id_, nombre, talla, cantidad, precio)
    productos.append(producto)
    print(f"El articulo {nombre} se agrego con exito!")
    print()

def elimina_producto(productos):
    print()
    id_ = int(input("¿Cual es el id que quieres eliminar?: "))
    producto_encontrado = False
    for producto in productos:
        if producto.id == id_:
            producto_encontrado = True
            break
    if producto_encontrado:
        productos.remove(producto)
        print(f"El articulo con id {id_} ha sido eliminado con exito!")
    else:
        print(f"El id {id_} no existe")
    print()

def exportar_a_json(productos):
    productos_exportar = [p.to_dict() for p in productos]
    with open(NOMBRE_JSON, "w") as arch_txt:
        json.dump(productos_exportar, arch_txt, indent=4)
    print("Los productos han sido exportados")
    print(f"Revise el archivo {NOMBRE_JSON}")

def importar_de_json():
    with open(NOMBRE_JSON) as arch_txt:
        datos = json.load(arch_txt)

    productos = []
    for p in datos:  # p es de tipo dict
        producto = Producto(
            p["id"],
            p["nombre"],
            p["talla"],
            p["cantidad"],
            p["precio"]
        )
        productos.append(producto)

    return productos