inventario = ["manzana", "leche", "pan"]
agregar = ["huevo", "queso"]
eliminar = ["pan"]

def actualizar_inventario(inventario, agregar, eliminar):
    inventario.extend(agregar)
    for elemento in eliminar:
        if elemento in inventario:
            inventario.remove(elemento)
        else:
            print(f"El elemento {elemento} no esta en el inventario")
    inventario.sort()
    return inventario

print(actualizar_inventario(inventario, agregar, eliminar))