# 📚 Guía Maestra de Estructuras de Datos en Python

### Teoría y práctica de Listas, Tuplas, Strings y Diccionarios — De cero a experto.

En Python, las estructuras de datos son la base para organizar y manipular información de manera eficiente. Comprender sus diferencias y casos de uso permite escribir código más claro, optimizado y profesional.

-----

## 📋 Tabla de Contenidos

1.  [Listas](https://www.google.com/search?q=%23-listas-lists)
2.  [Tuplas](https://www.google.com/search?q=%23-tuplas-tuples)
3.  [Strings](https://www.google.com/search?q=%23-strings)
4.  [Diccionarios](https://www.google.com/search?q=%23-diccionarios-dictionaries)
5.  [⚖️ Comparación General](https://www.google.com/search?q=%23%25EF%25B8%258F-diferencias-clave)
6.  [💡 Patrones para Entrevistas](https://www.google.com/search?q=%23-patrones-comunes-en-entrevistas-t%C3%A9cnicas)

-----

## 📋 Listas (Lists)

Las listas son colecciones **ordenadas y mutables**. Son dinámicas, permitiendo que sus elementos crezcan, se reduzcan o se modifiquen según sea necesario.

### 🔹 Propiedades

| Propiedad | Valor |
| :--- | :--- |
| **¿Mutable?** | ✅ Sí |
| **¿Ordenada?** | ✅ Sí |
| **¿Duplicados?** | ✅ Sí |
| **Acceso** | Índice numérico |

### 🛠️ Operaciones Esenciales

```python
# Creación
lista = [1, 2, 3]
lista = list("hola")       # ['h','o','l','a']

# Adición y Eliminación
lista.append(5)            # agrega al final
lista.insert(0, 99)        # inserta en índice dado
lista.pop()                # elimina y retorna el ÚLTIMO
lista.remove(5)            # elimina la PRIMERA ocurrencia del valor

# Ordenamiento
lista.sort()               # modifica la original
nueva = sorted(lista)      # retorna NUEVA lista
```

> ⚠️ **Trampa clásica:** `.sort()` modifica la original y retorna `None`. `sorted()` no toca la original y retorna una nueva lista.

### ✂️ Slicing y Copia

```python
t = [10, 20, 30, 40, 50]
t[1:3]     # [20, 30] (del índice 1 al 2)
t[::-1]    # [50, 40, 30, 20, 10] (invertir)

# Copia Real (Evita que ambas apunten al mismo objeto)
b = a.copy()    
b = a[:]        
```

-----

## 📦 Tuplas (Tuples)

Las tuplas son colecciones **ordenadas pero inmutables**. Son más eficientes en memoria y protegen los datos de modificaciones accidentales.

### 🔹 Propiedades

| Propiedad | Valor |
| :--- | :--- |
| **¿Mutable?** | ❌ No |
| **¿Ordenada?** | ✅ Sí |
| **¿Duplicados?** | ✅ Sí |
| **Casos de uso** | Coordenadas, configuraciones, retorno múltiple |

### 🛠️ Características Únicas

```python
# Creación (la coma es obligatoria para un solo elemento)
t = (1, 2, 3)
solo_uno = (5,) 

# Desestructuración: El superpoder de las tuplas
punto = (10, 20)
x, y = punto  # x=10, y=20

# Swap de variables sin temporal
a, b = b, a
```

-----

## 🔤 Strings

Un string es una cadena de texto **inmutable**. Cada operación de transformación crea un nuevo string en memoria.

### 🔹 Métodos de Transformación y Búsqueda

```python
s = "hola mundo"

s.upper()              # "HOLA MUNDO"
s.capitalize()         # "Hola mundo"
s.replace("h", "y")    # "yola mundo"
"Mundo" in s           # True (búsqueda booleana)

# Split y Join (Los más importantes)
lista_palabras = "a,b,c".split(",")    # ["a", "b", "c"]
unido = "-".join(["x", "y", "z"])      # "x-y-z"
```

-----

## 🗂️ Diccionarios (Dictionaries)

Almacenan información en formato **clave-valor**. Son mutables y ofrecen un acceso extremadamente rápido a los datos.

### 🔹 Propiedades

| Propiedad | Valor |
| :--- | :--- |
| **¿Mutable?** | ✅ Sí |
| **¿Ordenado?** | ✅ Sí (Python 3.7+) |
| **¿Duplicados?** | ❌ No (Claves únicas) |
| **Acceso** | Por clave (no índice) |

### 🛠️ Manejo de Datos

```python
d = {"nombre": "Luis", "edad": 25}

# Acceso seguro con .get()
d.get("altura", 1.70)  # Retorna 1.70 si no existe la clave

# Iteración eficiente
for clave, valor in d.items():
    print(f"{clave}: {valor}")

# Dict Comprehension
cuadrados = {x: x**2 for x in range(5)}
```

-----

## ⚖️ Diferencias Clave

| Estructura | Ordenada | Mutable | Acceso | Uso Principal |
| :--- | :--- | :--- | :--- | :--- |
| **Lista** | Sí | Sí | Índice | Colecciones dinámicas |
| **Tupla** | Sí | No | Índice | Datos constantes / Seguridad |
| **String** | Sí | No | Índice | Procesamiento de texto |
| **Diccionario**| Sí | Sí | Clave | Relación de datos (JSON-like) |

-----

## 💡 Patrones Comunes en Entrevistas Técnicas

1.  **Contar ocurrencias (Frecuencia):**
    ```python
    conteo = {}
    for x in lista:
        conteo[x] = conteo.get(x, 0) + 1
    ```
2.  **Invertir una secuencia:** `s[::-1]`
3.  **Filtrar datos (List Comprehension):**
    ```python
    pares = [x for x in range(10) if x % 2 == 0]
    ```
4.  **Comparar elementos adyacentes:**
    ```python
    for i in range(len(lista) - 1):
        if lista[i] == lista[i+1]: # Detectar duplicados seguidos
            ...
    ```

-----

