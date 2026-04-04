d = {}
d = dict()
d = dict(nombre="Fer", edad=1.56)
d = { "nombre" : "Luis", "edad": 25 }


# -- OBTENCION Y EDICION DE DATOS --
print("\n-- OBTENCION Y EDICION DE DATOS --\n")
print(d["nombre"])
print(d["edad"])
print(d.get("edad", 4)) # 4 valor por defecto si no existe

a = { "name": "Alfonso" }
a["age"] = 23
a["name"] = "Carlos"
a.update({"name" : "cristian", "age": 54})
a.update(name="Lima")

print(a["name"])
print(a["age"])

# -- 3 VISTAS PRINCIPALES -- 
print("\n-- 3 VISTAS PRINCIPALES -- \n")
b = { "a" : 1, "b" : 2, "c" : 3 }
print(b.keys())
print(b.values())
print(b.items())

print(list(b.keys()))
print(list(b.values()))
print(list(b.items()))

# -- RECORRER DICCIONARIOS --
print("\n-- RECORRER DICCIONARIOS --\n")

for clave in b:
    print(clave)

for valor in b.values():
    print(valor)
    
for c, v in b.items():
    print(f"{c} : {v}")


# COPIAR UN DICCIONARIO A OTRO:

d = {"a": 1, "b": 2}
d2 = d
d2 = d.copy() 
print(d[0])