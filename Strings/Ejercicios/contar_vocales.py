
def contar_vocales(s):
    vocales = "aeiou"
    count = 0
    for i in range(len(s)):
        if s[i] in vocales:
            count+=1
    return count


print(contar_vocales("hola"))
print(contar_vocales("Cristian"))
print(contar_vocales("ojo"))
print(contar_vocales("sk"))
print(contar_vocales("ejauoli"))