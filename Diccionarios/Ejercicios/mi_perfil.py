usuario = {
    "nombre": "Luis",
    "edad": 25,
    "ciudad": "La Paz"
}
usuario2 = {"nombre":"Ana","edad":30}

def describir_usuario(usuario):
    return f'{usuario.get("nombre")} tiene {usuario["edad"]} y vive en {usuario.get("ciudad", "desconocida")}'

print(describir_usuario(usuario))
print(describir_usuario(usuario2))