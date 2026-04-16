from invertir_cadena import invertir_cadena

def es_palindroma(s):
    original = s
    invertida = invertir_cadena(s)
    return original == invertida

print(es_palindroma("hola"))
print(es_palindroma("ojo"))
print(es_palindroma("ana"))
print(es_palindroma("Cristian"))
print(es_palindroma("oruro"))