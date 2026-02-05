# Escribir párrafos de código

Status: Modulo 3

# 1. Pasos Secuenciales (Sequential Steps)

Es la forma más básica de programación.

- **`Cómo funciona:`** El código se ejecuta **`línea por línea`**, de arriba hacia abajo, en el orden exacto en que fue escrito.
- **`Regla:`** No se salta ningún paso y no se repite nada.
- **`Ejemplo:`** Asignar un valor a x, luego imprimir x, luego sumar algo a x. El diagrama de flujo es una línea recta hacia abajo.

**Ejemplo en Python:**

```python
# Código Secuencial - Ejecución línea por línea
x = 5                    # Paso 1: Asignar valor
print("x =", x)          # Paso 2: Imprimir x
x = x + 3                # Paso 3: Sumar 3 a x
print("x ahora =", x)    # Paso 4: Imprimir resultado final
```

**`Características` del código secuencial:**

- Se ejecuta de arriba hacia abajo, sin saltos
- Cada línea se ejecuta exactamente una vez
- No hay decisiones ni repeticiones
- Es predecible: siempre produce el mismo resultado con las mismas entradas


# 2. Pasos Condicionales:

Aquí es donde el programa empieza a mostrar `inteligencia.`.

- **Palabra clave:** `if`
- **Cómo funciona:** El programa hace una **pregunta** (una condición lógica que resulta en Verdadero o Falso).
    - Si es **`Verdadera` (True):** Entra en el bloque de código indentado y lo ejecuta.
    - Si es **`Falsa` (False):** Se salta ese bloque de código completamente, como si no existiera, y continúa con lo que sigue.
- **Visualización:** En un diagrama de flujo, esto se ve como una bifurcación en el camino.

**Ejemplo en Python:**

```python
# Código Condicional - Toma de decisiones
edad = 18

if edad >= 18:
    print("Eres mayor de edad")
    print("Puedes votar")
else:
    print("Eres menor de edad")
    print("Aún no puedes votar")

print("Fin del programa")
```

**Características del código condicional:**

- El programa evalúa una condición (pregunta lógica)
- Si la condición es **True (Verdadera)**: ejecuta el bloque de código dentro del `if`
- Si la condición es **False (Falsa)**: se salta ese bloque y puede ejecutar el bloque `else` (si existe)
- El programa continúa después de la estructura condicional
- Permite que el programa tome decisiones basadas en datos



# 3. Pasos Repetitivos:

Este patrón permite a las computadoras hacer lo que mejor saben hacer: repetir tareas muchas veces sin cansarse.

- **Palabra clave:** `while` `for`.
- **Cómo funciona:** Funciona de manera similar a un if porque también hace una pregunta (condición).
    - Si es **Verdadera:** Ejecuta el bloque de código.
    - **La diferencia clave:** Al terminar de ejecutar el bloque, el flujo **vuelve a subir** al inicio para hacer la pregunta de nuevo.
    - Si es **Falsa:** Sale del bucle y continúa con el programa.

>👨🏻‍🏫  
>**Variable de Iteración:** El Dr. Chuck enfatiza que para evitar un "bucle infinito" (que nunca termina), necesitamos una variable que cambie dentro del bucle (por ejemplo, n = n - 1). Esto asegura que, en algún momento, la pregunta sea Falsa y el bucle termine.

**Ejemplo en Python con while:**

```python
# Código Repetitivo - Bucle while
n = 5

while n > 0:
    print("n =", n)
    n = n - 1  # Variable de iteración (evita bucle infinito)

print("¡Bucle terminado!")
print("n final =", n)
```

**Ejemplo en Python con for:**

```python
# Código Repetitivo - Bucle for
for i in range(5, 0, -1):
    print("i =", i)

print("¡Bucle terminado!")
print("i ya no existe fuera del bucle")
```

**Características del código repetitivo:**

- El programa evalúa una condición antes de cada iteración
- Si la condición es **True (Verdadera)**: ejecuta el bloque y **vuelve al inicio** del bucle
- Si la condición es **False (Falsa)**: sale del bucle y continúa con el resto del programa
- Requiere una **variable de iteración** que cambie en cada vuelta para evitar bucles infinitos
- Permite automatizar tareas repetitivas de manera eficiente



**Diferencia clave entre while y for:**

- **while:** Repite mientras una condición sea verdadera. Requiere que tú manejes la variable de iteración manualmente (ej: `n = n - 1`)
- **for:** Repite un número específico de veces o sobre una secuencia. Python maneja automáticamente la variable de iteración