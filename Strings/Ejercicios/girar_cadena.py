def girar(s, n):
    tam = len(s)
    c = list(s)
    aux = None
    if n == 0:
        return s
    if n > 0:
        for i in range(n):
            aux = c[0]
            for j in range(1, tam):
                c[j-1] = c[j]
            c[tam-1] = aux
    elif n < 0:  
        for i in range(-n):
            aux = c[tam-1]
            for j in range(tam-2, -1, -1):
                c[j+1] = c[j]
            c[0] = aux
    cadena = "".join(c)
    return cadena

print(girar("abc", 2))
print(girar("abc", -2))
    