# Listas
print("\nlistas: \n")

lista = [1,2,3,4]
lista_2 = [98,99,19]

print(lista)
print(lista_2)

print("\nAgregar elementos a una lista\n")
# append
lista.append(5)
lista.append(5)
print(lista)

# metodo count: cuenta cuantas veces aparece un valor
print()

# metodo index
print(lista.index(5))

# metodo extend
lista.extend(lista_2)
print(lista)

# metodo insert
lista.insert(0, 77) # index, numero insertado
print(lista)

print(f"\nMetodos de eliminacion: \n")
# metodo remove
print(f"\nMetodo remove: \n")

print(lista)
print(f"\nEliminando el primer 5: \n")
lista.remove(5) # Elimina el primer 5 encontrado no todos
print(lista)
print(f"\nEliminando el segundo 5: \n")
lista.remove(5) # Elimina el segundo 5 encontrado no todos
print(lista)

# metodo pop
lista.pop()
print(lista)

lista.pop(4)
print(lista)

# metodo clear
lista.clear()
print(lista)