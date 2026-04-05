s = {1,2,3}
print(s)
s = {1,2,3,3,3,4} # Elimina duplicados
print(s)
s = set() # crea set vacio = {} es para diccionarios
print(s)
s = set([1,2,3,4,4]) # Elimina duplivados
print(s)
s = set("hola")
print(s)

print("\n-- AGREGAR ELEMTOS Y ELIMINAR -- \n")
s = {1,2,3,5,6}
s.add(4) # añade 4
s.add(2) # como ya existe no añade pero no da error
print(s)

s.remove(2)
# s.remove(2) # da error si ya no existe
s.discard(3)
s.discard(2) # no rompe si no existe ya que elimina tambien
print(s)
s.pop() # elimina un elemento aleatorio
print(s)
s.clear() # vacia todo
print(s)

print("\n-- CONSULTA -- \n")
s = {1,2,3,4}
print(len(s))
print(2 in s) # mas rapido que en una lista
print(2 not in s)
print(9 in s)

print("\n-- OPERACIONES -- \n")
a = {1,2,3,4}
b = {4,5,6}
# union
print(a | b)
print(a.union(b))
# Interseccion -> los que estan en ambos
print(a & b)
print(a.intersection(b))
# Diferencia -> los que estan en a pero no en b
print(a - b)
print(a.difference(b))
# diferencia simetrica -> los que estan en uno pero no ambos
print(a ^ b)
print(a.symmetric_difference(b))

# a =       {1, 2, 3, 4}
# b =            { 3, 4, 5, 6}

# a | b  →  {1, 2, 3, 4, 5, 6}   todo
# a & b  →        {3, 4}          solo el medio
# a - b  →  {1, 2}               solo lo de a
# a ^ b  →  {1, 2,       5, 6}   los extremos

print("\n-- ACTUALIZA SIN CREAR UNO NUEVO -- \n")
a = {1, 2, 3}
b = {3, 4, 5}

a |= b                        # a = a | b  → {1,2,3,4,5}
a &= b                        # a = a & b
a -= b                        # a = a - b
a ^= b                        # a = a ^ b

a.update(b)                   # igual que |=
a.intersection_update(b)      # igual que &=
a.difference_update(b)        # igual que -=
a.symmetric_difference_update(b)  # igual que ^=

print("\n-- RECORRER UN CONJUNTO -- \n")

s = {1,2,3}
for elemento in s:
    print(elemento)

    
# Si necesitas un set que no cambie (para usarlo como clave de dict)
fs = frozenset([1, 2, 3])
# fs.add(4)       #  no tiene este método
d = {fs: "valor"}  #  puede ser clave de diccionario
print(d)
print(fs)