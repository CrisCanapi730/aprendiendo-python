puntajes_1 = [100, 80, 60, 40]
puntajes_2 = [0, 10, 20, 40]
puntajes_3 = [80, 100, 30, 68]

nuevo_1 = 70
nuevo_2 = 1
nuevo_3 = 110

def insertar_en_ranking(puntajes, nuevo):
    puntajes.append(nuevo)
    aux = None
    for j in range (len(puntajes) - 1):
        for i in range (len(puntajes) - 1):
            if puntajes[i] < puntajes[i+1]:
                # aux = puntajes[i]
                # puntajes[i] = puntajes[i+1]
                # puntajes[i+1] = aux
                puntajes[i], puntajes[i+1] = puntajes[i+1], puntajes[i]
    return puntajes

print(insertar_en_ranking(puntajes_1, nuevo_1))
print(insertar_en_ranking(puntajes_2, nuevo_2))
print(insertar_en_ranking(puntajes_3, nuevo_3))