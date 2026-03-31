lista = [5, 1, 9, 3, 9, 7, 5, 2]
n = 3

def top_n(lista, n):
    resultado = []
    lista_descendente = sorted(lista, reverse=True)
    for num in lista_descendente:
        if num not in resultado:
            resultado.append(num)
        if len(resultado) == n:
            break
    return resultado

print(top_n(lista, n))