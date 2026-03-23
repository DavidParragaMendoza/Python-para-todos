# Módulo 5 - Código condicional


# Condicionales - Parte 1

En este bloque, aprendemos cómo hacer que nuestros programas de Python dejen de ser solo una lista de instrucciones que se leen de arriba a abajo y comiencen a **tomar decisiones** por sí mismos.

- **La declaración `if`:** Es la forma en que Python hace una pregunta lógica. Si la respuesta a la pregunta es Verdadera, el programa ejecuta un bloque de código. Si es Falsa, lo ignora por completo.
- **Operadores de Comparación:** Para hacer estas preguntas, usamos operadores matemáticos simples:
    - **`<`** (Menor que) y **`<=`** (Menor o igual a)
    - **`>`** (Mayor que) y **`>=`** (Mayor o igual a)
    - **`==`** (Igual a). **`Un error muy común`** de novatos es usar un solo igual (**`=`**). En Python, **`=`** sirve para guardar un valor en una variable, mientras que **`==`** sirve para preguntar si dos cosas son iguales.
    - **`!=`** (Diferente de / No es igual a).
    
        ```python
        # Condicionales, Son estructuras de control que permiten ejecutar   
        # un bloque de código solo si se cumple una condición específica. 
        # En Python, se utilizan las palabras clave if, elif y else para 
        # crear condicionales.
        
        x=5
        if x >10:
            print('Smaller than 10')
        if x >20:
            print('Bigger than 20')
        
        print('Finished')
        
        ```
    
    >👨🏻‍🏫  
    >**La importancia de la Indentación (`Sangría`):** En Python, el espacio en blanco importa muchísimo. Para decirle a Python qué líneas de código pertenecen a un `if`, debemos “empujarlas” hacia la derecha (generalmente 4 espacios). Esto define el bloque de código.

    ```python
    #Operadores de comparación
    y=5
    if y==5:
        print('y es igual a 5')
    if y > 4:
        print('y es mayor que 4')
    if y >=5:
        print('y es mayor o igual a 5')
    if y < 6:
        print('y es menor que 6')
    if y<= 5:
        print('y es menor o igual a 5')
    if y!=6:
        print('y es diferente de 6')
    ```

- **Decisiones de dos caminos (`if` / `else`):** A veces queremos una bifurcación en el camino. "Si es verdadero, haz esto; **si no (`else`)**, haz esta otra cosa". El programa elige un camino u otro, pero nunca ambos.
    
    ```python
    #decisiones bidireccionales con else
    m=5
    if m>5:
        print('m es mayor que 5')
    else:
        print('m es menor o igual que 5')
    ```
    

- **Decisiones Anidadas:** Puedes poner un `if` dentro de otro `if`, como si fueran muñecas rusas (Matrioskas). Sirve para hacer preguntas más específicas solo si se cumplió la primera condición.
    
    ```python
    #Decisiones anidadas
    w=42
    if w>1:
        print('Mayor que 1')
        if w<100:
            print('Menor que 100')
    print('Fin del programa')
    
    ```
    

# Condicionales - Parte 2

A veces, la vida no es solo **`blanco o negro`**, sino que hay múltiples opciones. Para eso Python tiene la herramienta de decisiones múltiples.

- **La palabra clave `elif` (Else If / O si no, si...):** Nos permite encadenar varias preguntas lógicas seguidas.
- **`¿Cómo funciona?`** Python revisa las preguntas en orden, de arriba a abajo. **En el instante en que encuentra una condición verdadera, ejecuta ese bloque de código y se sale de toda la estructura.** No sigue revisando las demás opciones.
    
    
    >👨🏻‍🏫  
    >**El orden importa:** Si programas una condición como "Si es menor que 10" antes de "Si es menor que 2", y le pasas el número 1, Python se detendrá en la primera (porque 1 es menor que 10) y nunca llegará a revisar si es menor que 2. Diseñar bien el orden lógico es clave para que no haya código "muerto" (código que nunca se va a ejecutar).
    

- **La red de seguridad `else`:** Al final de una cadena de `elif`, puedes poner un `else` opcional. Actúa como un "cajón de sastre": si ninguna de las condiciones de arriba fue verdadera, se ejecuta esta por defecto.
    
    ```python
    #Decisiones múltiples con elif
    x=5
    if x<5:
        print('x es menor que 5')
    elif x==5:
        print('x es igual a 5')
    else:
        print('x es mayor que 5')
    ```
    

# La Estructura Try / Except:

Este es un concepto fundamental para crear programas "robustos" es decir que no se rompan fácilmente.

- **¿Cuál es el problema?** Si le pides a Python que convierta la palabra "Hola" en un número entero, Python entra en pánico, lanza un error gigante en pantalla, llamado **`Traceback`**, y **el programa se detiene por completo**. Para un usuario final, esto es una **`experiencia terrible`**.
- **La solución (`try` / `except`):** Funciona como una póliza de seguro.
    - Pones el código "peligroso", el que sospechas que podría fallar, como leer un dato ingresado por un usuario, dentro de un bloque llamado **`try` (intentar)**.
    - Le dices a Python: "Intenta hacer esto. Si funciona, genial, ignora el except. Pero si algo sale mal y vas a explotar, no te detengas; en su lugar, salta al bloque **`except` (excepción)**".

        ```python
        numero = input('Ingrese un número: ')
        try:
            valor = int(numero)
        except:
            valor = -1

        if valor >0:
            print('Es un número')
        else:
            print('No es un número válido')
        ```

>👨🏻‍🏫  
>No debes poner todo tu programa dentro de un `try`. Solo debes envolver esa línea de código específica que sabes que es riesgosa. 
