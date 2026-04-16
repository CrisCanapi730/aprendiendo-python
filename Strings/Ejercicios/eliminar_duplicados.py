def eliminar_duplicados(s):
    nueva = ""
    for c in s:
        if c in nueva:
            continue
        else:
            nueva+=c
    return nueva

print(eliminar_duplicados("aaggbbbbeeae"))
print(eliminar_duplicados("bbbbjjjjj"))
print(eliminar_duplicados("aassddffgggghhjj"))