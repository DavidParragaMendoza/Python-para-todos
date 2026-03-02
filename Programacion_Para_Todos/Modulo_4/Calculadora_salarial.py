#2.3 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
# Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25). 
# You should use input to read a string and float() to convert the string to a number. 
# Do not worry about error checking or bad user data.

#2.3 Escribe un programa para solicitar al usuario las horas y la tarifa por hora usando la entrada para calcular el salario bruto. 
# Usa 35 horas y una tarifa de 2.75 por hora para probar el programa (el pago debería ser 96.25). 
# Debes usar la entrada para leer una cadena y float() para convertir la cadena a un número. 
# No te preocupes por la verificación de errores o los datos de usuario incorrectos.
# This first line is provided for you

horas = input("Enter Hours:")
tarifa = input("Ingrese la tarifa")
salario = float(horas) * float(tarifa)
print("Pay:", salario)