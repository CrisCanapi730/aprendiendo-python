def comprimir(s):
    letras = ""
    cadena = ""
    for c in s:
        contador = 0
        i = 0
        while(s[i] == c):
            contador+=1
            i+=1
            
        cadena = cadena + c + str(contador)
    return cadena
print(comprimir("aabbccc"))