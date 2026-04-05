# Donde podemos usar
# Eliminar duplicados de una lista — la forma más rápida
lista = [1, 2, 2, 3, 3, 3, 4]
sin_duplicados = list(set(lista))   # [1, 2, 3, 4]

# Verificar existencia — set es MUCHO más rápido que lista
# En lista: recorre uno por uno → lento con listas grandes
1000 in [x for x in range(10000)]   # lento
# En set: acceso instantáneo sin importar el tamaño
1000 in set(range(10000))           # rápido

# Encontrar elementos en común entre dos listas
lista_a = [1, 2, 3, 4]
lista_b = [3, 4, 5, 6]
comunes = set(lista_a) & set(lista_b)   # {3, 4}

cadena = """
Método.   Qué hace
.add(x).   Agrega un elemento
.remove(x)  Elimina — error si no existe
.discard(x) Elimina — no rompe si no existe
.pop()  Elimina y retorna uno aleatorio
.clear()    Vacía el set
.union(b)   o |Todos los elementos de ambos
.intersection(b)    o &Solo los que están en ambos
.difference(b)  o -Los de a que no están en b
.symmetric_difference(b)    o ^Los que no están en ambos
.issubset(b)    ¿a está contenido en b?.
issuperset(b)   ¿a contiene a b?
.isdisjoint(b)  ¿No tienen nada en común?
.copy() Copia real del set.
update(b)   Agrega todos los de b a a

"""