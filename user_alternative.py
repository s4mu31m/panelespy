def max_paneles(at, lt, ap, lp):
    # Calculo de Primera orientacion (Panel a en paralelo al Techo)
    orientacion1 = (at // ap) * (lt // lp)
    orientacion1 += ((at%ap) // lp) * (lt // ap) + ((lt%lp) // ap) * (at // lp)
    # Calculo de Segunda orientacion (Panel b en paralelo a la Pared)
    orientacion2 = (at // lp) * (lt // ap)
    orientacion2 += ((at%lp) // ap) * (lt // lp) + ((lt%ap) // lp) * (at // ap)
    return max(orientacion1, orientacion2)

def solicitar_medidas():
    try:
        at = int(input("Ingrese el ancho del techo: "))
        lt = int(input("Ingrese el largo del techo: "))
        ap = int(input("Ingrese el ancho del panel solar: "))
        lp = int(input("Ingrese el largo del panel solar: "))
        
        if at <= 0 or lt <= 0 or ap <= 0 or lp <= 0:
            raise ValueError("Todas las medidas deben ser mayores a cero.")
        
        cantidad_maxima = max_paneles(at, lt, ap, lp)
        print(f"La cantidad máxima de paneles solares que caben en el techo es: {cantidad_maxima}")
    
    except ValueError as e:
        print(f"Entrada inválida: {e}. Por favor, ingrese números enteros positivos.")

# Ejemplo de uso
solicitar_medidas()
