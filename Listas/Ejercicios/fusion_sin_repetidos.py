lista_1 = [9,25,4,2,5,5,1]
lista_2 = [1,5,3,59,0]

def fusionar_listas(lista_1, lista_2):
    contador = 0
    lista_1.extend(lista_2)
    lista_1.sort()
    respuesta = []
    repetidos = []
    for num in lista_1:
        if num not in respuesta:
            respuesta.append(num)
        
        elif num not in repetidos:
            contador+=1
            repetidos.append(num)
                
    return respuesta, contador

print(fusionar_listas(lista_1, lista_2))