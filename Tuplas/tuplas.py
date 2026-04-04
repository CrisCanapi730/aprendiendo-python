# -- CREACION DE TUPLAS --
print("\n-- CREACION DE TUPLAS --\n")

t = (1,2,3)
print(t)
print(type(t))
t = 1,2,3
print(t)
t = (1)
print(t)
print(type(t))
t = (1,)
print(t)
t = tuple([1,2,3])
print(t)
t = ()
print(t)

# -- ACCESO DE TUPLAS --
print("\n-- ACCESO DE TUPLAS --\n")

t = (10, 20, 30, 40)
print(t[0])
print(t[-1])
print(t[1:3])
print(t[::-1])

# -- METODOS --
print("\n-- METODOS --\n")

t = (1,2,2,2,1,3,4)
print(t.count(2))
print(t.index(4))
print(len(t))

# -- FUNCIONES EXTRA --
print("\n-- FUNCIONES EXTRA --\n")

t = (1,2,3)
l = list(t)
print(t)
print(l)

print(t + (4,5))
print(t*2)
print(2 in t)