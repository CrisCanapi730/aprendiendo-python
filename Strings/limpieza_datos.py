s = "hola"
s_spaces = "    cris "
s_dot = "...fern.ando.."
frutas = "Uva Platano Manzana"
verduras = ["Lechuga", "Pepino", "Zanahoria"]
# -- ELIMINAR ESPACIOS
print("\n-- ELIMINAR ESPACIOS --\n")
print(s_spaces.strip()) # Elimina todos los espacios
print(s_spaces.lstrip()) # Elimina los espacios de la izquierda
print(s_spaces.rstrip()) # Elimina los espacios de la derecha
print(s_dot.strip(".")) # Elimina el caracter solo si esta al final o principio

# -- REMPLAZO Y DIVISION --
print("\n-- REMPLAZO Y DIVISION --\n")
print(f"String original: {s}")
print(s.replace("a","ee")) # remplaza a por ee
print(frutas.split(" ")) # separa los elementos por el caracter dado y los vuelve lista
print(frutas.split(" ", 1))
print("-".join(verduras))
print(",+".join(verduras))

