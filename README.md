📘 Proyecto de Optimización Numérica – Semestre 2025-1
👨‍💻 Autor:
Jhon Fredy Hoyos Cardenas
Estudiante de Ingeniería de Sistemas – Universidad de Antioquia

![image](https://github.com/user-attachments/assets/f5987242-db51-4129-8d1d-ce4f380013fd)

🎯 Descripción del Proyecto
Este proyecto implementa una interfaz gráfica en Python que permite aplicar y visualizar distintos métodos numéricos de optimización, tanto para búsqueda de raíces como para búsqueda de máximos/mínimos de funciones. Es una herramienta interactiva diseñada como parte del curso de Optimización (2025-1), ideal para aprender y comparar algoritmos clásicos.

🛠️ Métodos implementados
Método de Bisección

Método de Falsa Posición (Regla Falsa)

Método de la Razón Dorada (Golden Section Search)

Interpolación Cuadrática

Método de Newton

Método de Newton-Raphson (para extremos)

Búsqueda Aleatoria Multivariable

Cada método ofrece una salida tabular con los pasos del algoritmo, una gráfica de la función y una gráfica del error por iteración.

🖼️ Interfaz Gráfica
El programa usa Tkinter para la interfaz gráfica y matplotlib para graficar:

Ingreso dinámico de parámetros (función, intervalo, tolerancia, etc.)

Resultados tabulados en pantalla

Visualización del comportamiento del error

Gráficas de la función con estimaciones interactivas

▶️ Ejecución
Requisitos:

Python 3.10+

Librerías: sympy, numpy, matplotlib, tkinter (incluido por defecto en Python)

Clona este repositorio y ejecuta el archivo principal:

bash
Copiar
Editar
python Main.py
📂 Estructura del Proyecto
bash
Copiar
Editar
├── Main.py                         # Interfaz gráfica principal
├── Biseccion.py                   # Método de Bisección
├── FalsaPosicion.py              # Método de Falsa Posición
├── RazonDorada.py                # Razón Dorada (Golden Section)
├── InterpolacionCuadratica.py    # Interpolación cuadrática
├── Newton.py                     # Método de Newton
├── NewtonRaphson.py              # Método de Newton-Raphson (extremos)
├── BusquedaAleatoria.py          # Búsqueda Aleatoria en múltiples variables
📌 Notas
Las funciones deben ser ingresadas en formato compatible con sympy, por ejemplo:
x**2 - 4*x + 4, sin(x), exp(-x**2)

La búsqueda aleatoria permite funciones de varias variables: x**2 + y**2, con variables ingresadas como x, y.


📬 Contacto
📧 Gmail: frediicardenas1234@gmail.com
🔗 LinkedIn: [Fredy Cárdenas](https://www.linkedin.com/in/fredy-c%C3%A1rdenas-a4072731a/)

