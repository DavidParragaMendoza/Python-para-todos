#TRY / EXCEPT
astr = 'hola bob'
try:
    istr = int(astr)
except: 
    istr = 'ERROR DE TIPO'
print('Primero:', istr)

astr = '123'
try:
    istr = int(astr)
except:
    istr = -1
print('Segundo:', istr)


numero = input('Ingrese un número: ')
try:
    valor = int(numero)
except:
    valor = -1

if valor >0:
    print('Es un número')
else:
    print('No es un número válido')