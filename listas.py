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

# metodo extend
lista.extend(lista_2)
print(lista)

# metodo insert
lista.insert(0, 77) # index, numero insertado
print(lista)

# metodo remove
lista.remove(5) # Elimina el primer 5 encontrado no todos
print(lista)
lista.remove(5) # Elimina el segundo 5 encontrado no todos
print(lista)