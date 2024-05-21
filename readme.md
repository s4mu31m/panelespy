<!DOCTYPE html>
<html>
<head>
    <title>Solar Panel Placement Solution</title>
</head>
<body>
    <h1>Solar Panel Placement Solution</h1>
    <p>Este repositorio contiene dos algoritmos diferentes para resolver el problema de maximizar el número de paneles solares que se pueden colocar en un techo dado.</p>

    <h2>Archivos</h2>

    <h3>1. <code>function.py</code></h3>
    <p><code>function.py</code> contiene la función principal <code>max_paneles(at, lt, ap, lp)</code>, que calcula la máxima cantidad de paneles solares que se pueden colocar en un techo con dimensiones específicas. Este archivo se enfoca en la solución propuesta al problema, utilizando dos orientaciones posibles para colocar los paneles.</p>

    <p><strong>Función principal:</strong></p>
    <ul>
        <li><code>max_paneles(at, lt, ap, lp)</code>: Calcula la cantidad máxima de paneles solares que caben en el techo utilizando dos orientaciones diferentes y devuelve el valor máximo.</li>
    </ul>

    <p><strong>Ejemplo de uso:</strong></p>
    <pre>
<code>
print(max_paneles(2, 4, 1, 2))  # Debe retornar 4
print(max_paneles(3, 5, 1, 2))  # Debe retornar 7
print(max_paneles(10, 1, 2, 2)) # Debe retornar 0
</code>
    </pre>

    <h3>2. <code>user_alternative.py</code></h3>
    <p><code>user_alternative.py</code> ofrece una alternativa para validar el código con las medidas deseadas por el usuario. Además de la función <code>max_paneles(at, lt, ap, lp)</code>, este archivo incluye la función <code>solicitar_medidas()</code> que permite al usuario ingresar las dimensiones del techo y de los paneles solares interactuando directamente con el programa.</p>

    <p><strong>Funciones principales:</strong></p>
    <ul>
        <li><code>max_paneles(at, lt, ap, lp)</code>: Calcula la cantidad máxima de paneles solares que caben en el techo, similar a la función en <code>function.py</code>.</li>
        <li><code>solicitar_medidas()</code>: Solicita al usuario las dimensiones del techo y de los paneles solares, valida las entradas y muestra el resultado.</li>
    </ul>

    <p><strong>Ejemplo de uso:</strong></p>
    <pre>
<code>
# Ejecuta la función para solicitar medidas al usuario e imprimir el resultado
solicitar_medidas()
</code>
    </pre>

    <h2>Cómo ejecutar</h2>
    <ol>
        <li>Clona este repositorio:
            <pre>
<code>
git clone https://github.com/tu_usuario/solar-panel-placement.git
cd solar-panel-placement
</code>
            </pre>
        </li>
        <li>Para ejecutar la solución propuesta (<code>function.py</code>):
            <pre>
<code>
python function.py
</code>
            </pre>
        </li>
        <li>Para ejecutar la alternativa interactiva (<code>user_alternative.py</code>):
            <pre>
<code>
python user_alternative.py
</code>
            </pre>
        </li>
    </ol>

    <h2>Contribución</h2>
    <p>Si deseas contribuir a este proyecto, por favor crea un fork del repositorio y envía un pull request con tus mejoras y/o correcciones.</p>

    <h2>Licencia</h2>
    <p>Este proyecto está bajo la Licencia MIT. Consulta el archivo <a href="LICENSE">LICENSE</a> para más detalles.</p>
</body>
</html>
