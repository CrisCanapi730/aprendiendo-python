def comprimir(s):
    letra = None
    cadena = ""
    tam = len(s)
    i=0
    while(i<tam):
        contador = 0
        letra = s[i]
        j = i
        while(j<tam):
            if s[j] == letra:
                contador+=1
            else:
                break
            j+=1
        cadena = cadena + letra + str(contador)
        i = i + contador
    return cadena

print(comprimir("aabbbabcc"))