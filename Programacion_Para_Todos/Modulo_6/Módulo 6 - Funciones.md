# Módulo 6 - Funciones


## **`Parte 1:` ¿Qué son las funciones y el principio de "Guardar y Reutilizar"?**

En programación, a menudo nos encontramos escribiendo las mismas líneas de código una y otra vez. Para evitar esto, los programadores usan el principio de `"Guardar y Reutilizar"` (también conocido como `Don't Repeat Yourself` o **`DRY`**).

Una **`función`** es básicamente un **`bloque de código empaquetado`** y guardado bajo un nombre específico.  

- Es como una **`receta de cocina`**: la escribes una sola vez, pero puedes preparar el plato (ejecutar el código) todas las veces que quieras sin tener que volver a escribir las instrucciones paso a paso.

- 🔍 **Ejemplo de la vida real**
    
    Imagina el botón de "Hacer café" en una máquina. No necesitas saber cómo hierve el agua o cómo muele el grano; solo presionas el botón y la máquina hace esa "función".
    

- 💻 **Ejemplo en Python**
    
    Python ya trae funciones preconstruidas, como `max()`. Si le pasas la frase `"Hola mundo"` a **`max('Hola mundo')`**, la función escanea internamente las letras y te devuelve la letra más grande (en este caso, la `'w'`). Tú no tuviste que escribir el código para buscar letra por letra; simplemente `reutilizaste` la función **`max()`**.
    

---

## `Parte 2:` Creando nuestras propias funciones:

Además de usar las funciones que ya vienen en Python como `print()` para imprimir texto o `int()` para convertir texto a números, nosotros podemos `crear las nuestras`. Para esto usamos la palabra reservada **`def`** (que significa *definir*).

>👨🏻‍🏫  
>Definir una función **`NO significa que se va a ejecutar de inmediato`**. Cuando usas **`def`**, Python solo "memoriza" esos pasos. Para que el código realmente haga algo, tienes que **`llamar` o `invocar`** a la función por su nombre.

</aside>

### 🎵 Ejemplo práctico:

Imagina que creas una función para cantar una canción:

```python
def cantar():
    print("Soy un leñador y estoy muy bien...")
    print("Duermo toda la noche y trabajo todo el día.")
```

Si ejecutas eso, la pantalla `no mostrará nada`. Python solo guardó la canción en su memoria. Para que cante, debes invocarla así:

```python
cantar()  # Aquí es donde realmente se imprime la letra en pantalla
```

---

## `Parte 3:` Entradas y Salidas:

Las funciones pueden ser aún más inteligentes si les damos `información para trabajar` y les pedimos que nos devuelvan un `resultado útil`.

- **📥 Entradas (Parámetros/Argumentos):** Son los datos que le pasamos a la función dentro de los paréntesis. Le permiten a la función hacer su trabajo de manera `personalizada`.
- **📤 Salidas (Valor de retorno):** Es el resultado que la función "escupe" hacia afuera después de hacer su trabajo. Para esto se usa la palabra mágica **`return`**. Cuando Python lee `return`, `detiene la función` y envía el resultado de vuelta.
- 🥤 **Ejemplo de la vida real**
    
    Es como una `máquina expendedora`. Tú introduces una moneda (esa es la **entrada** o argumento) y la máquina te expulsa un refresco (ese es el **retorno** o resultado).
    

### 🌍 Ejemplo en Python:

```python
def saludar(idioma):
    if idioma == 'es':
        return 'Hola'
    elif idioma == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

# Usando la función:
saludo_espanol = saludar('es')
print(saludo_espanol, "Carlos")  # Imprimirá: Hola Carlos
```

Aquí, **`es`** es el argumento que entra, y **`Hola`** es el valor que retorna la función para que podamos usarlo en el resto de nuestro programa.