
def ordenar_cadena(s):
    l = list(s)
    tam = len(s)
    for i in range(tam-1):
        for j in range(tam-1-i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    cadena = "".join(l)
    return cadena
            

def anagrama(s, c):
    s = s.lower()
    c = c.lower()
    so = ordenar_cadena(s)
    co = ordenar_cadena(c)
    return so == co

print(anagrama("salir", "raliS"))
print(anagrama("hola", "casa"))
print(anagrama("rata", "atar"))
print(anagrama("AMOR", "roma"))
print(anagrama("cris", "lechiga"))
