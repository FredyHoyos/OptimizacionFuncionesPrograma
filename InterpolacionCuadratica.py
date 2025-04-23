import sympy as sp

class InterpolacionCuadratica:
    def __init__(self, funcion_str, x0, x1, x2, iter_max, tol, opcion_minimo):
        self.funcion_str = funcion_str
        self.x0 = x0
        self.x1 = x1
        self.x2 = x2
        self.iter_max = iter_max
        self.tol = tol
        self.errores = []
        self.iteraciones = []
        self.resultados = []
        self.datos = []
        self.opcion_minimo = opcion_minimo

        self.x = sp.symbols('x')
        self.funcion = sp.sympify(funcion_str)

    def calcular_x3(self, f0, f1, f2, x0, x1, x2):
        """Calcular el siguiente valor x3 según la interpolación cuadrática."""
        try:
            return (f0 * (x1 ** 2 - x2 ** 2) + f1 * (x2 ** 2 - x0 ** 2) + f2 * (x0 ** 2 - x1 ** 2)) / (
                2 * f0 * (x1 - x2) + 2 * f1 * (x2 - x0) + 2 * f2 * (x0 - x1))
        except:
            return 0.0

    def calcular(self):
        try:
            f0 = float(self.funcion.subs(self.x, self.x0).evalf())
            f1 = float(self.funcion.subs(self.x, self.x1).evalf())
            f2 = float(self.funcion.subs(self.x, self.x2).evalf())
            x3 = self.calcular_x3(f0, f1, f2, self.x0, self.x1, self.x2)
            f3 = float(self.funcion.subs(self.x, x3).evalf())
            error = abs(x3 - self.x2)
            self.iteraciones.append(0)
            self.errores.append(error)
            self.resultados.append((0, self.x0, f0, self.x1, f1, self.x2, f2, x3, f3, error))

            i = 1
            while i <= self.iter_max and error > self.tol:

                if self.opcion_minimo == "Mínimo":
                    if f3 > f1:
                        self.x2, self.x1 = self.x1, x3
                    else:
                        self.x0, self.x1 = self.x1, x3
                else:
                    if f3 < f1:
                        self.x2, self.x1 = self.x1, x3
                    else:
                        self.x0, self.x1 = self.x1, x3

                f0 = float(self.funcion.subs(self.x, self.x0).evalf())
                f1 = float(self.funcion.subs(self.x, self.x1).evalf())
                f2 = float(self.funcion.subs(self.x, self.x2).evalf())
                x3 = self.calcular_x3(f0, f1, f2, self.x0, self.x1, self.x2)
                f3 = float(self.funcion.subs(self.x, x3).evalf())
                error = abs(x3 - self.x2)

                self.iteraciones.append(i)
                self.errores.append(error)
                self.resultados.append((i, self.x0, f0, self.x1, f1, self.x2, f2, x3, f3, error))

                i += 1

            if self.opcion_minimo == "Mínimo":
                self.datos = [("Iter", "x0", "f0", "x1", "f1", "x2", "f2", "x3", "f3", "Error"),
                              f"El mínimo se encuentra en x3 = {x3}"]
            else:
                self.datos = [("Iter", "x0", "f0", "x1", "f1", "x2", "f2", "x3", "f3", "Error"),
                              f"El máximo se encuentra en x3 = {x3}"]

            return self.resultados, self.iteraciones, self.errores, x3, error, self.datos
        except sp.SympifyError:
            raise ValueError("La función ingresada no es válida.")
        except Exception as e:
            raise RuntimeError(f"Error inesperado: {str(e)}")
