
import sympy as sp
import numpy as np
import random


class BusquedaAleatoria:
    def __init__(self, funcion_str, variables, iter_max, tol, rango_min, rango_max):
        self.funcion_str = funcion_str
        self.variables = variables
        self.iter_max = iter_max
        self.tol = tol
        self.rango_min = rango_min
        self.rango_max = rango_max
        self.errores = []
        self.iteraciones = []
        self.resultados = []
        self.datos = []
        self.simbolos = sp.symbols(variables)
        self.funcion = sp.sympify(funcion_str)

    def calcular(self):
        try:
            mejor_x = np.array([random.uniform(self.rango_min, self.rango_max) for _ in self.simbolos])
            mejor_f = float(self.funcion.subs(dict(zip(self.simbolos, mejor_x))).evalf())
            self.resultados.append((0, *mejor_x, mejor_f))
            self.iteraciones.append(0)
            self.errores.append(float('inf'))

            for i in range(1, self.iter_max + 1):
                nuevo_x = np.array([random.uniform(self.rango_min, self.rango_max) for _ in self.simbolos])
                nuevo_f = float(self.funcion.subs(dict(zip(self.simbolos, nuevo_x))).evalf())
                error = abs(nuevo_f - mejor_f)

                if nuevo_f < mejor_f:
                    mejor_x = nuevo_x
                    mejor_f = nuevo_f

                self.iteraciones.append(i)
                self.errores.append(error)
                self.resultados.append((i, *nuevo_x, nuevo_f))

                if error < self.tol:
                    break

            self.datos = [("Iter", *self.variables.split(), "f(x)"), f"El mínimo se encuentra en x = {mejor_x}"]
            return self.resultados, self.iteraciones, self.errores, mejor_x, mejor_f, self.datos
        except sp.SympifyError:
            raise ValueError("La función ingresada no es válida.")
        except Exception as e:
            raise RuntimeError(f"Error inesperado: {str(e)}")