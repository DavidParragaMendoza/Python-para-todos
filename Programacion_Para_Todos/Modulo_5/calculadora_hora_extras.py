hora_trabajada = float(input("Ingrese la cantidad de horas trabajadas: ")) #45
pago_por_hora = float(input("Ingrese el pago por hora: ")) #10.50
if hora_trabajada >40:
    hora_extra = hora_trabajada - 40 #5
    valor_1 = (hora_trabajada - hora_extra) * pago_por_hora #45 -5 *10.50 = 40 * 10.50 = 420
    valor_2 = hora_extra * (pago_por_hora * 1.5) #5 * (10.50 * 1.5) = 5 * 15.75 = 78.75
    pago_total = valor_1 + valor_2 
else:
    pago_total = hora_trabajada * pago_por_hora

print("El pago total es: ", pago_total)
