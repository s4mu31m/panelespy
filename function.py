def max_paneles(at, lt, ap, lp):
    # Calculo de Primera orientacion (Panel a en paralelo al Techo)
    orientacion1 = (at // ap) * (lt // lp)
    orientacion1 += ((at%ap) // lp) * (lt // ap) + ((lt%lp) // ap) * (at // lp)
    # Calculo de Segunda orientacion (Panel b paralelo al techo)
    orientacion2 = (at // lp) * (lt // ap)
    orientacion2 += ((at%lp) // ap) * (lt // lp) + ((lt%ap) // lp) * (at // ap)
    return max(orientacion1, orientacion2)

print(max_paneles(2, 4, 1, 2))  # Debe retornar 4
print(max_paneles(3, 5, 1, 2))  # Debe retornar 7
print(max_paneles(10, 1, 2, 2)) # Debe retornar 0
 