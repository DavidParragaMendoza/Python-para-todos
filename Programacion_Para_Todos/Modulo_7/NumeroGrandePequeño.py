#5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, 
# print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch 
# it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

#5.  2 Escribe un programa que solicite repetidamente al usuario números enteros hasta que el usuario introduzca 'done'. 
# Una vez que se introduce 'done', imprime el mayor y el menor de los números. Si el usuario introduce algo que no sea un número válido, 
# captúralo con un try/except e imprime un mensaje apropiado e ignora el número. Introduce 7, 2, bob, 10 y 4 y haz que coincida 
# con la salida que aparece a continuación.
#Invalid input
#Maximum is 10
#Minimum is 2
maximum = None
minimum = None
while True:
    numero = input("Escriba un número: ")
    if numero == 'done':
        break
    try:
        value = int(numero)
    except:
        print("Invalid input")
        continue

    #numero mayor
    if maximum is None:
        maximum = value
    elif value > maximum:
        maximum = value
    #numero menor
    if minimum is None:
        minimum = value
    elif value < minimum:
        minimum = value

print("Maximum is", maximum)
print("Minimum is", minimum)