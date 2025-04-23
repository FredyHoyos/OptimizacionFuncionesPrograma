import tkinter as tk
from tkinter import messagebox

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from tkinter import Label
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from Biseccion import Biseccion
from BusquedaAleatoria import BusquedaAleatoria
from FalsaPosicion import FalsaPosicion
from InterpolacionCuadratica import InterpolacionCuadratica
from Newton import MetodoNewton
from NewtonRaphson import NewtonRaphson
from RazonDorada import BusquedaRazonAurea


def metodo_biseccion():
    try:
        funcion_str = entrada_funcion1.get()
        xl = float(entrada_xl1.get())
        xu = float(entrada_xu1.get())
        iter_max = int(entrada_itera1.get())
        tol = float(entrada_error1.get())

        biseccion = Biseccion(funcion_str, xl, xu, iter_max, tol)
        resultados, iteraciones, errores, raiz, error_final, encabezados = biseccion.calcular()

        mostrar_resultados(resultados,encabezados)
        mostrar_graficas(funcion_str, xl, xu, iteraciones, errores)

        lbl_resultado1["text"] = encabezados[1]
        lbl_resultado1["background"] = "lightcoral"

        messagebox.showinfo("Resultado", f"Raíz encontrada: {raiz:.4f} con un error de {error_final:.12f}")

    except ValueError as e:
        messagebox.showerror("Error", str(e))
    except RuntimeError as e:
        messagebox.showerror("Error inesperado", str(e))

def metodo_falsa_posicion():
    try:
        funcion_str = entrada_funcion2.get()
        xl = float(entrada_xl2.get())
        xu = float(entrada_xu2.get())
        iter_max = int(entrada_itera2.get())
        tol = float(entrada_error2.get())

        falsaPosicion = FalsaPosicion(funcion_str, xl, xu, iter_max, tol)
        resultados, iteraciones, errores, raiz, error_final, encabezados = falsaPosicion.calcular()

        mostrar_resultados(resultados,encabezados)
        mostrar_graficas(funcion_str, xl, xu, iteraciones, errores)

        lbl_resultado2["text"] = encabezados[1]
        lbl_resultado2["background"] = "lightcoral"

        messagebox.showinfo("Resultado", f"Raíz encontrada: {raiz:.4f} con un error de {error_final:.12f}")

    except ValueError as e:
        messagebox.showerror("Error", str(e))
    except RuntimeError as e:
        messagebox.showerror("Error inesperado", str(e))

def metodo_razon_dorada():
    try:
        funcion_str = entrada_funcion3.get()
        xl = float(entrada_xl3.get())
        xu = float(entrada_xu3.get())
        iter_max = int(entrada_itera3.get())
        tol = float(entrada_error3.get())
        opcion = str(opcion3.get())

        busquedaRazonAurea = BusquedaRazonAurea(funcion_str, xl, xu, iter_max, tol, opcion)
        resultados, iteraciones, errores, dato, error_final, encabezados = busquedaRazonAurea.calcular()

        mostrar_resultados(resultados,encabezados)
        mostrar_graficas(funcion_str, xl, xu, iteraciones, errores)

        lbl_resultado3["text"] = encabezados[1]
        lbl_resultado3["background"] = "lightcoral"

        if opcion == "Mínimo":
            messagebox.showinfo("Resultado", f"El mínimo es: {dato:.4f} con un error de {error_final:.12f}")
        else:
            messagebox.showinfo("Resultado", f"El máximo es: {dato:.4f} con un error de {error_final:.12f}")

    except ValueError as e:
        messagebox.showerror("Error", str(e))
    except RuntimeError as e:
        messagebox.showerror("Error inesperado", str(e))


def metodo_interpolacion_cuadratica():
    try:
        funcion_str = entrada_funcion4.get()
        x04 = float(entrada_x04.get())
        x24 = float(entrada_x24.get())
        x14 = float(entrada_x14.get())
        iter_max = int(entrada_itera4.get())
        tol = float(entrada_error4.get())
        opcion = str(opcion4.get())

        interpolacionCuadratica = InterpolacionCuadratica(funcion_str, x04, x14, x24, iter_max, tol, opcion)
        resultados, iteraciones, errores, dato, error_final, encabezados = interpolacionCuadratica.calcular()

        mostrar_resultados(resultados,encabezados)
        mostrar_graficas(funcion_str, x04, x24, iteraciones, errores)

        lbl_resultado4["text"] = encabezados[1]
        lbl_resultado4["background"] = "lightcoral"

        if opcion == "Mínimo":
            messagebox.showinfo("Resultado", f"El mínimo es: {dato:.4f} con un error de {error_final:.12f}")
        else:
            messagebox.showinfo("Resultado", f"El máximo es: {dato:.4f} con un error de {error_final:.12f}")

    except ValueError as e:
        messagebox.showerror("Error", str(e))
    except RuntimeError as e:
        messagebox.showerror("Error inesperado", str(e))

def metodo_newton():
    try:
        funcion_str = entrada_funcion5.get()
        x5 = float(entrada_x5.get())
        iter_max = int(entrada_itera5.get())
        tol = float(entrada_error5.get())

        newton = MetodoNewton(funcion_str, x5, iter_max, tol)
        resultados, iteraciones, errores, dato, error_final, encabezados = newton.calcular()

        mostrar_resultados(resultados,encabezados)
        mostrar_graficas(funcion_str, x5-5, x5+5, iteraciones, errores)

        lbl_resultado5["text"] = encabezados[1]
        lbl_resultado5["background"] = "lightcoral"

        messagebox.showinfo("Resultado", f"La raíz es: {dato:.4f} con un error de {error_final:.12f}")

    except ValueError as e:
        messagebox.showerror("Error", str(e))
    except RuntimeError as e:
        messagebox.showerror("Error inesperado", str(e))

def metodo_newton_raphson():
    try:
        funcion_str = entrada_funcion6.get()
        x6 = float(entrada_x6.get())
        iter_max = int(entrada_itera6.get())
        tol = float(entrada_error6.get())

        newtonRaphson = NewtonRaphson(funcion_str, x6, iter_max, tol)
        resultados, iteraciones, errores, dato, error_final, encabezados, tipo = newtonRaphson.calcular()

        mostrar_resultados(resultados,encabezados)
        mostrar_graficas(funcion_str, x6-5, x6+5, iteraciones, errores)

        lbl_resultado6["text"] = encabezados[1]
        lbl_resultado6["background"] = "lightcoral"

        messagebox.showinfo("Resultado", f"El {tipo} es: {dato:.4f} con un error de {error_final:.12f}")

    except ValueError as e:
        messagebox.showerror("Error", str(e))
    except RuntimeError as e:
        messagebox.showerror("Error inesperado", str(e))

def metodo_busqueda_aleatoria():
    try:
        funcion_str = entrada_funcion7.get()
        variables = entrada_variables7.get()
        iter_max = int(entrada_itera7.get())
        tol = float(entrada_error7.get())
        rango_min = float(entrada_rango_min.get())
        rango_max = float(entrada_rango_max.get())

        busqueda = BusquedaAleatoria(funcion_str, variables, iter_max, tol, rango_min, rango_max)
        resultados, iteraciones, errores, mejor_x, mejor_f, encabezados = busqueda.calcular()

        mostrar_resultados(resultados, encabezados)
        mostrar_graficas(funcion_str, rango_min, rango_max, iteraciones, errores)

        lbl_resultado7["text"] = encabezados[1]
        lbl_resultado7["background"] = "lightcoral"

        messagebox.showinfo("Resultado", f"El mínimo encontrado es: {mejor_x} con f(x) = {mejor_f:.4f}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))
    except RuntimeError as e:
        messagebox.showerror("Error inesperado", str(e))

def mostrar_resultados(resultados, encabezados):
    text_resultados.delete("1.0", tk.END)

    # Encabezado dinámico (usando la primera fila de resultados como referencia)
    if not resultados:
        return

    header = " ".join(f"{col:<14}" for col in encabezados[0]) + "\n"
    text_resultados.insert(tk.END, header)

    # Insertar datos dinámicamente
    for res in resultados:
        fila = " ".join(
            f"{float(val):<14.9g}" if isinstance(val, (float, int, sp.Basic)) else str(val) for val in res) + "\n"
        text_resultados.insert(tk.END, fila)



def mostrar_graficas(funcion_str, xl, xu, iteraciones, errores):
    # Intentar convertir la función
    try:
        x = sp.symbols('x')
        funcion = sp.sympify(funcion_str)
        variables = funcion.free_symbols

        # Limpiar el frame antes de dibujar o mostrar mensaje
        for widget in frame_grafico.winfo_children():
            widget.destroy()

        if len(variables) > 1:
            # Mostrar mensaje si hay más de una variable
            mensaje = Label(frame_grafico, text="La función tiene múltiples variables. No se puede graficar en 2D.", fg="red", font=("Arial", 12))
            mensaje.pack()
            return

        # Función lambdificada para evaluar numéricamente
        f_lambdified = sp.lambdify(x, funcion, 'numpy')
        x_vals = np.linspace(xl - 5, xu + 5, 400)
        y_vals = f_lambdified(x_vals)

        # Crear figura
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

        # Gráfica de la función
        ax1.plot(x_vals, y_vals, label=f"${sp.latex(funcion)}$", color='r')
        ax1.axhline(0, color='black', linewidth=1, linestyle='--')
        ax1.axvline(0, color='black', linewidth=1, linestyle='--')
        ax1.set_title("Gráfica de la Función")
        ax1.set_xlabel("x")
        ax1.set_ylabel("f(x)")
        ax1.legend()
        ax1.grid(True)

        # Gráfica del error
        ax2.plot(iteraciones, errores, marker='o', linestyle='-', color='b', label='Error')
        ax2.set_xlabel("Iteraciones")
        ax2.set_ylabel("Error")
        ax2.set_title("Gráfica del Error")
        ax2.legend()
        ax2.grid(True)

        # Mostrar en Tkinter
        canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
        canvas.draw()
        canvas.get_tk_widget().pack()

    except Exception as e:
        # Mostrar error genérico si algo falla
        mensaje = Label(frame_grafico, text=f"Error al graficar: {str(e)}", fg="red", font=("Arial", 12))
        mensaje.pack()


def show_frame(frame, active_button):
    global active_frame, frame_resultados_grafica
    # Llevar el frame al frente
    frame.tkraise()
    # Actualizar la variable global
    active_frame = frame

    # Restaurar el color de todos los botones
    for btn in buttons:
        btn.config(bg="SystemButtonFace")  # Color original predeterminado

    # Cambiar el color del botón activo
    active_button.config(bg="lightgreen")

    # Si ya existe el contenedor de resultados, lo destruimos
    if frame_resultados_grafica is not None:
        frame_resultados_grafica.destroy()

    # Creamos el contenedor para resultados y gráficas en el frame activo
    frame_resultados_grafica = tk.Frame(active_frame)
    frame_resultados_grafica.grid(row=4, column=0, columnspan=10, pady=10, sticky="nsew")

    # Configurar el frame para que se expanda verticalmente
    frame_resultados_grafica.grid_rowconfigure(0, weight=1)
    frame_resultados_grafica.grid_rowconfigure(1, weight=1)
    frame_resultados_grafica.grid_columnconfigure(0, weight=1)

    # --- Primera fila: Resultados ---
    frame_texto = tk.Frame(frame_resultados_grafica)
    frame_texto.grid(row=0, column=0, sticky="nsew", padx=5)

    # Widget Text para mostrar los resultados
    global text_resultados  # Si lo usarás en otras funciones
    text_resultados = tk.Text(frame_texto, wrap="word", width=155, height=10)
    text_resultados.pack(side="left", fill="both", expand=True)

    # Scrollbar para el Text
    scrollbar = tk.Scrollbar(frame_texto, command=text_resultados.yview)
    scrollbar.pack(side="right", fill="y")
    text_resultados.config(yscrollcommand=scrollbar.set)

    # --- Segunda fila: Gráficas ---
    global frame_grafico  # Si lo usarás para actualizar gráficos luego
    frame_grafico = tk.Frame(frame_resultados_grafica, bg="white", width=600, height=300)
    frame_grafico.grid(row=5, column=0, sticky="nsew", padx=5, pady=5)


frame_resultados_grafica = None


def cerrar_ventana():
    # Aquí puedes agregar cualquier acción que desees antes de cerrar, como confirmaciones.
    root.quit()  # O root.destroy() si prefieres finalizar inmediatamente.

root = tk.Tk()
root.title("Métodos de optimización______Hecho por: Jhon Fredy Hoyos Cardenas 1045025784 Estudiante ing Sistemas UdeA________")
root.geometry("1470x700")

# Establecer la función para manejar el cierre de la ventana
root.protocol("WM_DELETE_WINDOW", cerrar_ventana)


# Contenedor principal para el contenido (frames superpuestos)
container = tk.Frame(root)
container.pack(side="right", fill="both", expand=True)

# Crear frames para el contenido principal
frames = []
for _ in range(7):
    frame = tk.Frame(container)
    frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
    frames.append(frame)

frame1, frame2, frame3, frame4, frame5, frame6, frame7 = frames

########################################################################################################################
# Contenido para frame1
lbl_xu1 = tk.Label(frame1, text=" Método de Bisección", background="lightblue")
lbl_xu1.grid(row=0, column=4)

lbl_funcion1 = tk.Label(frame1, text="Función f(x):")
lbl_funcion1.grid(row=1, column=0)
entrada_funcion1 = tk.Entry(frame1, width=30)
entrada_funcion1.insert(0, "3*x**2-120*x+100")
entrada_funcion1.grid(row=1, column=1)

lbl_xl1 = tk.Label(frame1, text=" Límite Inferior (xl):")
lbl_xl1.grid(row=1, column=2)
entrada_xl1 = tk.Entry(frame1, width=6)
entrada_xl1.insert(0, "-10")
entrada_xl1.grid(row=1, column=3)

lbl_xu1 = tk.Label(frame1, text=" Límite Superior (xu):")
lbl_xu1.grid(row=1, column=4)
entrada_xu1 = tk.Entry(frame1, width=6)
entrada_xu1.insert(0, "20")
entrada_xu1.grid(row=1, column=5)

lbl_xu1 = tk.Label(frame1, text=" Iteraciones:")
lbl_xu1.grid(row=1, column=6)
entrada_itera1 = tk.Entry(frame1, width=6)
entrada_itera1.insert(0, "20")
entrada_itera1.grid(row=1, column=7)

lbl_xu1 = tk.Label(frame1, text=" Error máximo:")
lbl_xu1.grid(row=1, column=8)
entrada_error1 = tk.Entry(frame1, width=12)
entrada_error1.insert(0, "0.000006")
entrada_error1.grid(row=1, column=9)

btn_calcular1 = tk.Button(frame1, text="Calcular", command=metodo_biseccion, background="lightgreen")
btn_calcular1.grid(row=2, column=2, pady=10)

lbl_resultado1 = tk.Label(frame1, text=" Resultado:...", background="lightgray")
lbl_resultado1.grid(row=2, column=6)
########################################################################################################################


########################################################################################################################
# Contenido para frame2
lbl_xu2 = tk.Label(frame2, text=" Método de Falsa posición", background="lightblue")
lbl_xu2.grid(row=0, column=4)

lbl_funcion2 = tk.Label(frame2, text="Función f(x):")
lbl_funcion2.grid(row=1, column=0)
entrada_funcion2 = tk.Entry(frame2, width=30)
entrada_funcion2.insert(0, "3*x**2-120*x+100")
entrada_funcion2.grid(row=1, column=1)

lbl_xl2 = tk.Label(frame2, text=" Límite Inferior (xl):")
lbl_xl2.grid(row=1, column=2)
entrada_xl2 = tk.Entry(frame2, width=6)
entrada_xl2.insert(0, "-10")
entrada_xl2.grid(row=1, column=3)

lbl_xu2 = tk.Label(frame2, text=" Límite Superior (xu):")
lbl_xu2.grid(row=1, column=4)
entrada_xu2 = tk.Entry(frame2, width=6)
entrada_xu2.insert(0, "20")
entrada_xu2.grid(row=1, column=5)

lbl_xu2 = tk.Label(frame2, text=" Iteraciones:")
lbl_xu2.grid(row=1, column=6)
entrada_itera2 = tk.Entry(frame2, width=6)
entrada_itera2.insert(0, "20")
entrada_itera2.grid(row=1, column=7)

lbl_xu2 = tk.Label(frame2, text=" Error máximo:")
lbl_xu2.grid(row=1, column=8)
entrada_error2 = tk.Entry(frame2, width=12)
entrada_error2.insert(0, "0.000006")
entrada_error2.grid(row=1, column=9)

btn_calcular2 = tk.Button(frame2, text="Calcular", command=metodo_falsa_posicion, background="lightgreen")
btn_calcular2.grid(row=2, column=2, pady=10)

lbl_resultado2 = tk.Label(frame2, text=" Resultado:...", background="lightgray")
lbl_resultado2.grid(row=2, column=6)
########################################################################################################################


########################################################################################################################
# Contenido para frame3
lbl_xu3 = tk.Label(frame3, text=" Método de la razón dorada", background="lightblue")
lbl_xu3.grid(row=0, column=4)

lbl_funcion3 = tk.Label(frame3, text="Función f(x):")
lbl_funcion3.grid(row=1, column=0)
entrada_funcion3 = tk.Entry(frame3, width=30)
entrada_funcion3.insert(0, "2 * sin(x) - x**2 / 10")
entrada_funcion3.grid(row=1, column=1)

lbl_xl3 = tk.Label(frame3, text=" Límite Inferior (xl):")
lbl_xl3.grid(row=1, column=2)
entrada_xl3 = tk.Entry(frame3, width=6)
entrada_xl3.insert(0, "0")
entrada_xl3.grid(row=1, column=3)

lbl_xu3 = tk.Label(frame3, text=" Límite Superior (xu):")
lbl_xu3.grid(row=1, column=4)
entrada_xu3 = tk.Entry(frame3, width=6)
entrada_xu3.insert(0, "4")
entrada_xu3.grid(row=1, column=5)

lbl_xu3 = tk.Label(frame3, text=" Iteraciones:")
lbl_xu3.grid(row=1, column=6)
entrada_itera3 = tk.Entry(frame3, width=6)
entrada_itera3.insert(0, "20")
entrada_itera3.grid(row=1, column=7)

lbl_xu3 = tk.Label(frame3, text=" Error máximo:")
lbl_xu3.grid(row=1, column=8)
entrada_error3 = tk.Entry(frame3, width=12)
entrada_error3.insert(0, "0.000006")
entrada_error3.grid(row=1, column=9)

opcion3 = tk.StringVar(value="Máximo")
tk.Radiobutton(frame3, text="Máximo", variable=opcion3, value="Máximo").grid(row=2, column=0)
tk.Radiobutton(frame3, text="Mínimo", variable=opcion3, value="Mínimo").grid(row=2, column=1)

btn_calcular3 = tk.Button(frame3, text="Calcular", command=metodo_razon_dorada, background="lightgreen")
btn_calcular3.grid(row=2, column=4, pady=10)

lbl_resultado3 = tk.Label(frame3, text=" Resultado:...", background="lightgray")
lbl_resultado3.grid(row=2, column=6)
########################################################################################################################


########################################################################################################################
# Contenido para frame4
lbl_xu4 = tk.Label(frame4, text=" Método de la Interpolación cuadrática", background="lightblue")
lbl_xu4.grid(row=0, column=4)

lbl_funcion4 = tk.Label(frame4, text="Función f(x):")
lbl_funcion4.grid(row=1, column=0)
entrada_funcion4 = tk.Entry(frame4, width=30)
entrada_funcion4.insert(0, "2 * sin(x) - x**2 / 10")
entrada_funcion4.grid(row=1, column=1)

lbl_x04 = tk.Label(frame4, text=" Límite Inferior (x0):")
lbl_x04.grid(row=1, column=2)
entrada_x04 = tk.Entry(frame4, width=6)
entrada_x04.insert(0, "0")
entrada_x04.grid(row=1, column=3)

lbl_x24 = tk.Label(frame4, text=" Límite Superior (x2):")
lbl_x24.grid(row=1, column=4)
entrada_x24 = tk.Entry(frame4, width=6)
entrada_x24.insert(0, "4")
entrada_x24.grid(row=1, column=5)

lbl_x14 = tk.Label(frame4, text=" Valor medio (x1):")
lbl_x14.grid(row=1, column=6)
entrada_x14 = tk.Entry(frame4, width=6)
entrada_x14.insert(0, "1")
entrada_x14.grid(row=1, column=7)

opcion4 = tk.StringVar(value="Máximo")
tk.Radiobutton(frame4, text="Máximo", variable=opcion4, value="Máximo").grid(row=2, column=0)
tk.Radiobutton(frame4, text="Mínimo", variable=opcion4, value="Mínimo").grid(row=2, column=1)

lbl_xu4 = tk.Label(frame4, text=" Iteraciones:")
lbl_xu4.grid(row=2, column=2)
entrada_itera4 = tk.Entry(frame4, width=6)
entrada_itera4.insert(0, "20")
entrada_itera4.grid(row=2, column=3)

lbl_xu4 = tk.Label(frame4, text=" Error máximo:")
lbl_xu4.grid(row=2, column=4)
entrada_error4 = tk.Entry(frame4, width=12)
entrada_error4.insert(0, "0.000006")
entrada_error4.grid(row=2, column=5)

btn_calcular4 = tk.Button(frame4, text="Calcular", command=metodo_interpolacion_cuadratica, background="lightgreen")
btn_calcular4.grid(row=2, column=6, pady=10)

lbl_resultado4 = tk.Label(frame4, text=" Resultado:...", background="lightgray")
lbl_resultado4.grid(row=2, column=7)
########################################################################################################################


########################################################################################################################
# Contenido para frame5
lbl_xu5 = tk.Label(frame5, text=" Método de Newton", background="lightblue")
lbl_xu5.grid(row=0, column=4)

lbl_funcion5 = tk.Label(frame5, text="Función f(x):")
lbl_funcion5.grid(row=1, column=0)
entrada_funcion5 = tk.Entry(frame5, width=30)
entrada_funcion5.insert(0, "2 * sin(x) - x**2 / 10")
entrada_funcion5.grid(row=1, column=1)

lbl_x5 = tk.Label(frame5, text=" Valor de (x):")
lbl_x5.grid(row=1, column=2)
entrada_x5 = tk.Entry(frame5, width=6)
entrada_x5.insert(0, "2.5")
entrada_x5.grid(row=1, column=3)

lbl_xu25 = tk.Label(frame5, text=" Iteraciones:")
lbl_xu25.grid(row=1, column=4)
entrada_itera5 = tk.Entry(frame5, width=6)
entrada_itera5.insert(0, "20")
entrada_itera5.grid(row=1, column=5)

lbl_x15 = tk.Label(frame5, text=" Error máximo:")
lbl_x15.grid(row=1, column=6)
entrada_error5 = tk.Entry(frame5, width=12)
entrada_error5.insert(0, "0.000006")
entrada_error5.grid(row=1, column=7)

btn_calcular5 = tk.Button(frame5, text="Calcular", command=metodo_newton, background="lightgreen")
btn_calcular5.grid(row=2, column=3, pady=10)

lbl_resultado5 = tk.Label(frame5, text=" Resultado:...", background="lightgray")
lbl_resultado5.grid(row=2, column=5)
########################################################################################################################


########################################################################################################################
# Contenido para frame6
lbl_xu6 = tk.Label(frame6, text=" Método de Newton Raphson", background="lightblue")
lbl_xu6.grid(row=0, column=4)

lbl_funcion = tk.Label(frame6, text="Función f(x):")
lbl_funcion.grid(row=1, column=0)
entrada_funcion6 = tk.Entry(frame6, width=30)
entrada_funcion6.insert(0, "2 * sin(x) - x**2 / 10")
entrada_funcion6.grid(row=1, column=1)

lbl_x6 = tk.Label(frame6, text=" Valor de (x):")
lbl_x6.grid(row=1, column=2)
entrada_x6 = tk.Entry(frame6, width=6)
entrada_x6.insert(0, "2.5")
entrada_x6.grid(row=1, column=3)

lbl_xu26 = tk.Label(frame6, text=" Iteraciones:")
lbl_xu26.grid(row=1, column=4)
entrada_itera6 = tk.Entry(frame6, width=6)
entrada_itera6.insert(0, "20")
entrada_itera6.grid(row=1, column=5)

lbl_x16 = tk.Label(frame6, text=" Error máximo:")
lbl_x16.grid(row=1, column=6)
entrada_error6 = tk.Entry(frame6, width=12)
entrada_error6.insert(0, "0.000006")
entrada_error6.grid(row=1, column=7)

btn_calcular6 = tk.Button(frame6, text="Calcular", command=metodo_newton_raphson, background="lightgreen")
btn_calcular6.grid(row=2, column=3, pady=10)

lbl_resultado6 = tk.Label(frame6, text=" Resultado:...", background="lightgray")
lbl_resultado6.grid(row=2, column=5)
########################################################################################################################


########################################################################################################################
# Contenido para frame7 (Búsqueda Aleatoria)
lbl_titulo7 = tk.Label(frame7, text=" Método de Búsqueda Aleatoria", background="lightblue")
lbl_titulo7.grid(row=0, column=4)

lbl_funcion7 = tk.Label(frame7, text="Función f(...):")
lbl_funcion7.grid(row=1, column=0)
entrada_funcion7 = tk.Entry(frame7, width=30)
entrada_funcion7.insert(0, "x**2 + y**2")  # Función de prueba
entrada_funcion7.grid(row=1, column=1)

lbl_variables7 = tk.Label(frame7, text="Variables (x, y, ...):")
lbl_variables7.grid(row=1, column=2)
entrada_variables7 = tk.Entry(frame7, width=10)
entrada_variables7.insert(0, "x, y")  # Variables separadas por coma
entrada_variables7.grid(row=1, column=3)

lbl_rango_min = tk.Label(frame7, text="Rango mín:")
lbl_rango_min.grid(row=1, column=4)
entrada_rango_min = tk.Entry(frame7, width=6)
entrada_rango_min.insert(0, "-5")
entrada_rango_min.grid(row=1, column=5)

lbl_rango_max = tk.Label(frame7, text="Rango máx:")
lbl_rango_max.grid(row=1, column=6)
entrada_rango_max = tk.Entry(frame7, width=6)
entrada_rango_max.insert(0, "5")
entrada_rango_max.grid(row=1, column=7)

lbl_iteraciones7 = tk.Label(frame7, text="Iteraciones:")
lbl_iteraciones7.grid(row=2, column=0)
entrada_itera7 = tk.Entry(frame7, width=6)
entrada_itera7.insert(0, "100")
entrada_itera7.grid(row=2, column=1)

lbl_error7 = tk.Label(frame7, text="Error máximo:")
lbl_error7.grid(row=2, column=3)
entrada_error7 = tk.Entry(frame7, width=12)
entrada_error7.insert(0, "0.0001")
entrada_error7.grid(row=2, column=4)

btn_calcular7 = tk.Button(frame7, text="Calcular", command=metodo_busqueda_aleatoria, background="lightgreen")
btn_calcular7.grid(row=3, column=4, pady=10)

lbl_resultado7 = tk.Label(frame7, text=" Resultado:...", background="lightgray")
lbl_resultado7.grid(row=3, column=6)
########################################################################################################################


########################################################################################################################
# Crear el menú lateral
frame_menu = tk.Frame(root, width=150, bg="gray")
frame_menu.pack(side="left", fill="y")

buttons = []  # Lista para almacenar los botones
btn_texts = ["Bisección", "Falsa Posición", "Razón Aurea", "Interpolación Cuadrática", "Newton", "Newton Raphson", "Búsqueda Aleatoria"]

# Crear botones dinámicamente
for i, text in enumerate(btn_texts):
    btn = tk.Button(frame_menu, text=text, command=lambda f=frames[i], b=None: show_frame(f, b))
    btn.pack(pady=10, padx=10, fill="x")
    buttons.append(btn)
    btn.config(command=lambda f=frames[i], b=btn: show_frame(f, b))  # Asignar función correcta


########################################################################################################################

########################################################################################################################
# Mostrar inicialmente el primer frame
show_frame(frame1, buttons[0])
root.mainloop()
########################################################################################################################