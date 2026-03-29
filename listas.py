# Listas
print("\n-- LISTAS CREADAS --: \n")

lista = [1,2,3,4]
lista_2 = [98,99,19]

print(lista)
print(lista_2)

print("\n-- METODOS DE ADICION --\n")
# append
print(f"Metodo append, agregando dos 5:")
lista.append(5)
lista.append(5)
print(lista)

# metodo count: cuenta cuantas veces aparece un valor
print(f"\nMetodo count:")
print(f"El numero 5 aparece {lista.count(5)} veces")

# metodo index
print(f"\nmetodo index")
print(f"La primera posicion encontrada para el numero 5 es {lista.index(5)}")
print(lista)

# metodo extend
print(f"\nMetodo extend")
print("Agregando lista 2 a lista 1")
lista.extend(lista_2)
print(lista)

# metodo insert
print(f"\nMetodo insert")
print("Agregando un elemento a una posicion dada")
lista.insert(0, 77) # index, numero insertado
print(lista)

print(f"\n-- METODOS DE ELIMINACION --")
# metodo remove
print(f"\nMetodo remove:")

print(lista)
print(f"\nEliminando el primer 5:")
lista.remove(5) # Elimina el primer 5 encontrado no todos
print(lista)
print(f"\nEliminando el segundo 5:")
lista.remove(5) # Elimina el segundo 5 encontrado no todos
print(lista)

# metodo pop
print(f"\nMetodo pop, elimina el ultimo elemento:")
lista.pop()
print(lista)

print(f"\nMetodo pop, elimina el elemento del indice dado:")
lista.pop(4)
print(lista)

# metodo clear
print(f"\nElimina toda las lista y la deja vacia:")
lista.clear()
print(lista)