#Decisiones múltiples con elif
x=5
if x<5:
    print('x es menor que 5')
elif x==5:
    print('x es igual a 5')
else:
    print('x es mayor que 5')


#Error común: Olvidar el bloque else
y=5
if y>5:
    print('y es mayor que 5')
elif y<25:
    print('y es menor que 25')

else:
    print('y es igual a 25')