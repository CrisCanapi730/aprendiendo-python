lista_1 = [1, 2, 4, 9, 3, 4, 1, 2]
lista_2 = [5, 5, 5, 5]
lista_3 = [1, 2, 3]
lista_4 = [1, 2, 7, 2, 3, 2, 7, 8, 1]

def eliminar_duplicados(lista):
    for i in range(len(lista) -1, -1, -1):
        i_count = lista.count(lista[i])
        if i_count > 1:
            lista.pop(i)
    return lista

print(eliminar_duplicados(lista_1))
print(eliminar_duplicados(lista_2))
print(eliminar_duplicados(lista_3))
print(eliminar_duplicados(lista_4))