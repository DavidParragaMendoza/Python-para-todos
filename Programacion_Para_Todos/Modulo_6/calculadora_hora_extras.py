def computepay(h, r):
    if h >40:
        he = h - 40 #5
        valor_1 = (h - he) * r #45 -5 *10.50 = 40 * 10.50 = 420
        valor_2 = he * (r * 1.5) #5 * (10.50 * 1.5) = 5 * 15.75 = 78.75
        pago_total = valor_1 + valor_2 
        return pago_total
    else:
        return  h * r



hora_trabajada = float(input("Ingrese la cantidad de horas trabajadas: ")) #45
pago_por_hora = float(input("Ingrese el pago por hora: ")) #10.50

pago_total = computepay(hora_trabajada, pago_por_hora)

print("El pago total es: ", pago_total)
