## 🏗️ Estructuras de Datos en Python

Las estructuras de datos son contenedores que nos permiten organizar y manipular información. Elegir la correcta depende de si necesitas modificar los datos, el orden en que se guardan y cómo deseas acceder a ellos.

### 📋 1. Listas (Lists)
Son las herramientas más flexibles de Python. Imagínalas como un archivador donde puedes añadir, quitar o cambiar carpetas en cualquier momento.
* **Naturaleza:** Ordenadas y **mutables** (modificables).
* **Uso ideal:** Cuando tienes una colección de elementos que cambiará con el tiempo, como una lista de tareas o resultados de un cálculo.
* **Acceso:** Se llega a cada elemento mediante su posición numérica (índice).

### 📦 2. Tuplas (Tuples)
Son similares a las listas, pero con un "candado". Una vez que se cierran, no se pueden alterar.
* **Naturaleza:** Ordenadas e **inmutables** (no se pueden cambiar).
* **Uso ideal:** Para datos que deben permanecer protegidos, como coordenadas geográficas $(x, y)$ o configuraciones fijas del sistema.
* **Ventaja:** Son más rápidas y consumen menos memoria que las listas.

### 🗂️ 3. Diccionarios (Dictionaries)
Funcionan como un catálogo o una agenda telefónica. En lugar de buscar por posición, buscas por una etiqueta específica.
* **Naturaleza:** Estructura de **clave-valor** y mutables.
* **Uso ideal:** Para organizar datos relacionados, como el perfil de un usuario (Nombre: "Ana", Edad: 25, Ciudad: "Madrid").
* **Acceso:** No usas números de posición, sino la "clave" única para obtener el "valor" asociado.

### 🔤 4. Cadenas de Texto (Strings)
Son secuencias de caracteres que representan palabras o mensajes.
* **Naturaleza:** Ordenadas e **inmutables**. Aunque parezca que las editas, Python crea una copia nueva cada vez que aplicas un cambio.
* **Uso ideal:** Manejo de cualquier información textual, mensajes al usuario o procesamiento de nombres.
* **Versatilidad:** Python ofrece herramientas potentes para buscar, limpiar y dar formato al texto de forma sencilla.

---

## ⚖️ Cuadro Comparativo

| Estructura | ¿Se puede modificar? | ¿Importa el orden? | Forma de acceso |
| :--- | :--- | :--- | :--- |
| **Lista** | ✅ Sí | ✅ Sí | Posición (Índice) |
| **Tupla** | ❌ No | ✅ Sí | Posición (Índice) |
| **Diccionario** | ✅ Sí | ✅ Sí* | Clave única |
| **String** | ❌ No | ✅ Sí | Posición (Carácter) |

> \* *Nota: En versiones modernas de Python, los diccionarios mantienen el orden en que se insertaron las claves.*



---
**Conclusión:** La clave del éxito en Python es saber qué herramienta sacar de la caja: **listas** para flexibilidad, **tuplas** para seguridad, **diccionarios** para relaciones rápidas y **strings** para comunicación.