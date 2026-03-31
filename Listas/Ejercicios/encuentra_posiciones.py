lista = [1, 5, 3, 5, 2, 5]
objetivo = 5

def encontrar_todas_posiciones(lista, objetivo):
    resultado = []
    for i in range(len(lista)):
        if lista[i] == objetivo:
            resultado.append(i)
    return resultado

print(encontrar_todas_posiciones(lista, objetivo))
print(encontrar_todas_posiciones(lista, 99))