
def invertir_cadena(s):
    aux = None
    cadena_original = s
    cadena_lista = list(s)
    tam = len(s)
    
    for i in range(tam//2):
        aux = cadena_lista[i]
        cadena_lista[i] = cadena_lista[tam-1-i]
        cadena_lista[tam-1-i] = aux
    
    cadena = "".join(cadena_lista)
    return cadena
    
# invertir_cadena("hola")
# invertir_cadena("ana")
# invertir_cadena("Cristian")