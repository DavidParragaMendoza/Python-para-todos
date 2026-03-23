# Módulo 7 - Bucles e iteración

# **`Parte 1:`** Bucles Indefinidos:

## **¿Qué es?**

Un bucle `while` (mientras) es como una declaración `if` (si) que se repite. Se le llama "indefinido" porque, al momento de escribir el código, no sabemos exactamente cuántas veces se va a ejecutar; simplemente seguirá corriendo *mientras* una condición lógica sea verdadera (`True`).

## **¿Cómo funciona?**

1. Python evalúa la condición (ej. `n > 0`).
2. Si es verdadera, ejecuta el bloque de código indentado.
3. Al terminar el bloque, **vuelve a subir** y evalúa la condición nuevamente.
4. Si la condición nunca se vuelve falsa (`False`), el programa se queda atrapado en un **bucle infinito** (hasta que se acabe la batería, la memoria o fuerces su cierre). Por eso es vital incluir una **variable de iteración**: un valor que cambie dentro del bucle (como `n = n - 1`) para asegurar que la condición eventualmente sea falsa y el bucle termine.

### **Ejemplo (Cuenta regresiva):**

```python
n = 5
while n > 0:
    print(n)
    n = n - 1  # Variable de iteración
print('Blastoff!')
```

### **Ejemplo (Bucle Infinito - Error común):**

```python
n = 5
while n > 0:
    print('Lather')
    print('Rinse')
    # n nunca cambia, por lo que n > 0 siempre es True
```

---

# **`Parte 2:`** Control del flujo de ejecución:

## **¿Qué es?**

A veces necesitamos tener un control más fino sobre un bucle `while` en tiempo real, sin tener que esperar a que el código vuelva a evaluar la condición principal en la parte superior. Para esto usamos comandos de escape.

## **¿Cómo funcionan?**

- **El teletransportador (`break`):** Cuando Python lee la palabra `break`, literalmente **destruye el bucle**. Abandona inmediatamente el bloque de código y salta a la primera línea que está *fuera* y *después* del bucle. Es ideal para bucles estructurados como `while True:` (que en teoría son infinitos), permitiendo que el bucle se detenga solo cuando el usuario escribe una palabra clave como "fin".
- **El botón de saltar (`continue`):** Cuando Python lee `continue`, no destruye el bucle, pero **aborta la iteración actual**. Ignora cualquier código que esté por debajo, salta inmediatamente a la parte superior del bucle y vuelve a evaluar la condición para iniciar el siguiente ciclo. Es muy útil para "filtrar" o ignorar ciertas líneas de datos que no nos interesan sin detener todo el programa.

### Ejemplos:

- **`break`:** Termina el bucle actual inmediatamente y salta a la línea de código que le sigue.
    
    ```python
    while True: # Bucle intencionalmente infinito
        line = input('> ')
        if line == 'done':
            break # Escapa del bucle
        print(line)
    print('Done!')
    ```
    
- **`continue`:** Abandona la iteración actual y vuelve al inicio del bucle para la siguiente iteración.
    
    ```python
    while True:
        line = input('> ')
        if line[0] == '#':
            continue # Salta el resto del código y vuelve arriba
        if line == 'done':
            break
        print(line)
    ```
    

---

# **`Parte 3:`** Bucles Definidos (`for`)

## **¿Qué es?**

Un bucle `for` (para) es un bucle "definido" porque se ejecuta una cantidad de veces fija y predecible. Se usa exclusivamente cuando tienes una **colección o secuencia de elementos** (una lista de números, los caracteres de una palabra, las líneas de un documento).

## **¿Cómo funciona?**

Aquí no tienes que crear lógica condicional ni actualizar variables manualmente para evitar bucles infinitos. Python hace el trabajo pesado usando la estructura `for [variable] in [colección]:`.
El bucle toma la variable de iteración y le asigna el valor del **primer** elemento de la colección, ejecuta el código, luego le asigna el valor del **segundo** elemento, y así sucesivamente. Cuando se queda sin elementos en la colección, el bucle termina de forma automática y segura. Es la forma más limpia de procesar grandes cantidades de datos.

### **Ejemplo (Iterando sobre una lista de números):**

```python
for i in [5, 4, 3, 2, 1]:
    print(i)
print('Blastoff!')
```

### **Ejemplo (Iterando sobre cadenas):**

```python
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)
```

---

# **`Parte 4:`** La `"Inteligencia"` de los Bucles (Patrones de Programación)

## **¿Qué es?**

Los bucles por sí solos solo repiten código. Para que hagan cosas útiles (como contar, sumar o encontrar promedios), los programadores usamos patrones clásicos llamados "Idioms".

## **¿Cómo funciona el patrón?**

El truco radica en entender que el bucle solo "ve" un elemento a la vez. Para que el programa tenga "memoria" del panorama completo, dividimos el trabajo en tres fases:

1. **Antes del bucle:** Inicializamos una variable.
2. **Durante el bucle:** Hacemos algo con cada elemento nuevo frente a nuestra variable.
3. **Después del bucle:** Imprimimos el resultado final que quedó almacenado en nuestra variable. ¡La magia ocurre en cómo la variable va evolucionando con cada vuelta!

### **Ejemplo Contar elementos:**

```python
count = 0
for thing in [9, 41, 12, 3, 74, 15]:
    count = count + 1
print('Cantidad de elementos:', count)
```

### **Ejemplo Encontrar el número mayor**

Usamos una variable para almacenar "el mayor que hemos visto hasta ahora".

```python
largest_so_far = -1
for the_num in[9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
print('El mayor es:', largest_so_far)
```

---

# **`Parte 5:`** Búsquedas Complejas, la variable `None` y el operador `is`

## **¿Qué es?**

Cuando queremos encontrar el **número menor** en una lista, el patrón anterior falla. Si inicializamos nuestra variable en **`-1`** y le pasamos una lista de números positivos, el **`-1`** siempre será el menor, dándonos un resultado falso. Necesitamos una forma de decirle al programa: *"Este es el primer número que veo, tómalo como el menor por ahora porque no tengo con qué compararlo"*.

## **¿Cómo funciona?**

Para solucionar esto, Python tiene un tipo de dato llamado **`None`**, que representa la nada absoluta (una variable vacía).

- Iniciamos con **`menor = None`**.
- En la primera iteración, al ver que **`menor`** es **`None`**, Python captura el primer número de la lista (ej. el 9).
- En las siguientes iteraciones, como **`menor`** ya no es **`None`** (ahora es 9), simplemente compara si el nuevo número es más pequeño que el que ya tiene guardado.

**El operador `is`:** Para comprobar si algo es `None`, no usamos `==`, usamos `is`. `is` es un operador lógico súper fuerte que no solo verifica si dos cosas valen lo mismo, sino si son **exactamente el mismo objeto** en la memoria del ordenador.

- **El operador `is`:** Es un operador lógico similar a `==` pero mucho más estricto. Revisa si dos variables apuntan exactamente al mismo objeto en memoria.

### **Ejemplo (Encontrar el número menor usando `None`):**

```python
smallest = None # Bandera inicial vacía
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None: # Solo será True en la primera iteración
        smallest = value
    elif value < smallest:
        smallest = value
print('El menor es:', smallest)
```

---