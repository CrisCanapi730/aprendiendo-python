def formatear_nom(n):
    n = n.strip(" ")
    l = n.split(" ")
    nom = ", ".join(l)
    nom = nom.title()
    return nom
print(formatear_nom(" sebastian oJeda "))
