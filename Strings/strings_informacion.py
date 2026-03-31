# -- CREACION DE STRINGS --
print("\n-- CREACION DE STRINGS --") 

nombre = "Cristian Canapi"
parrafo = """ Esto
es
un      parrafo"""
numeros = str(123)

print(nombre, parrafo, numeros)

# -- CONSULTAR INFORMACION DEL STRING --
print("\n-- CONSULTAR INFORMACION DEL STRING --")

print(f"El tamaño del nombre es: {len(nombre)}")
print(f"La letra a aparece: {nombre.count('a')} veces")
print(nombre.find("pi")) # indice donde empieza, -1 si no existe
print(nombre.find("ya")) # buscando una seccion del string que no existe
print(nombre.index("ri")) # igual pero lanza error si no existe
print(nombre.index("pi"))
print(nombre.startswith("Cr")) # Devuelve un bool si empieza con
print(nombre.startswith("r"))
print(nombre.endswith("pi")) # Devuelve un bool si termina con
print(nombre.endswith("o"))

# -- MAYUSCULAS Y MINUSCULAS --
print("\n-- MAYUSCULAS Y MINUSCULAS --")

print(f"Todo mayuscula: {nombre.upper()}")
print(f"Todo minuscula: {nombre.lower()}")
print(f"Primera letra del string mayuscula: {nombre.capitalize()}")
print(f"Primera letra de cada palabra mayuscula: {nombre.title()}")
print(f'Invierte todo al reves: {"letrA".swapcase()}')