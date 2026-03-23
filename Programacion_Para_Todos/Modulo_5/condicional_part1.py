# Condicionales, Son estructuras de control que permiten ejecutar un bloque de código solo si se cumple una condición específica. En Python, se utilizan las palabras clave if, elif y else para crear condicionales.
x=5
if x >10:
    print('Smaller than 10')
if x >20:
    print('Bigger than 20')

print('Finished')

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


#decisiones unilaterales
z=5
print('Antes 5')
if z==5:
    print ('z es igual a 5')
    print('Despues 5')
print('Despues de la condicion')
print('Antes 6')
if z==6:
    print('z es igual a 6')
    print('Despues 6')
print('Despues de la condicion')


#Decisiones anidadas
w=42
if w>1:
    print('Mayor que 1')
    if w<100:
        print('Menor que 100')
print('Fin del programa')

#decisiones bidireccionales con else
m=5
if m>5:
    print('m es mayor que 5')
else:
    print('m es menor o igual que 5')