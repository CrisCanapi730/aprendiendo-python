
def encontrar_sub(s):
    tam = len(tam)
    l = list(s)
    i = 0
    cad = ""
    count = 0
    # abababc
    while(i<tam):
        if s[i] not in cad:
            cad+=s[i]
            count+=1
        elif s[i] in cad:
            i = count