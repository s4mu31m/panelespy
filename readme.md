# Solar Panel Placement Solution

Este repositorio contiene dos algoritmos diferentes para resolver el problema de maximizar el número de paneles solares que se pueden colocar en un techo dado.

## Archivos

### 1. `function.py`

`function.py` contiene la función principal `max_paneles(at, lt, ap, lp)`, que calcula la máxima cantidad de paneles solares que se pueden colocar en un techo con dimensiones específicas. Este archivo se enfoca en la solución propuesta al problema, utilizando dos orientaciones posibles para colocar los paneles.

**Función principal:**
- `max_paneles(at, lt, ap, lp)`: Calcula la cantidad máxima de paneles solares que caben en el techo utilizando dos orientaciones diferentes y devuelve el valor máximo.

**Ejemplo de uso:**
```python
print(max_paneles(2, 4, 1, 2))  # Debe retornar 4
print(max_paneles(3, 5, 1, 2))  # Debe retornar 7
print(max_paneles(10, 1, 2, 2)) # Debe retornar 0
```
### 2. `user_alternative.py`

`user_alternative.py` ofrece una alternativa para validar el código con las medidas deseadas por el usuario. Además de la función `max_paneles(at, lt, ap, lp)`, este archivo incluye la función `solicitar_medidas()` que permite al usuario ingresar las dimensiones del techo y de los paneles solares interactuando directamente con el programa.

**Funciones principales:**
- `max_paneles(at, lt, ap, lp)`: Calcula la cantidad máxima de paneles solares que caben en el techo utilizando dos orientaciones diferentes y devuelve el valor máximo.
- `solicitar_medidas()`: Solicita al usuario las dimensiones del techo y de los paneles solares, valida las entradas y muestra el resultado.

**Ejemplo de uso:**
```python
# Ejecuta la función para solicitar medidas al usuario e imprimir el resultado
solicitar_medidas()
