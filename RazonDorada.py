import sympy as sp

class BusquedaRazonAurea:
    def __init__(self, funcion_str, xl, xu, iter_max, tol, opcion_minimo):
        self.funcion_str = funcion_str
        self.xl = xl
        self.xu = xu
        self.iter_max = iter_max
        self.tol = tol
        self.errores = []
        self.iteraciones = []
        self.resultados = []
        self.datos = []
        self.opcion_minimo = opcion_minimo
        self.x = sp.symbols('x')
        self.funcion = sp.sympify(funcion_str)

    def calcular(self):
        try:

            aureo = (1 + 5**0.5) / 2  # Razón dorada inversa
            invAureo = aureo -1
            a = invAureo * (self.xu - self.xl)
            b = invAureo * invAureo * (self.xu - self.xl)
            x1 = self.xl + a
            x2 = self.xl + b
            d = invAureo * (self.xu - self.xl)
            f1 = self.funcion.subs(self.x, x1).evalf()
            f2 = self.funcion.subs(self.x, x2).evalf()
            error = abs(x2 - x1)
            self.iteraciones.append(0)
            self.errores.append(error)
            self.resultados.append((0, self.xl, self.xu, d, x1, x2, f1, f2, error))
            i = 1
            while i <= self.iter_max and error > self.tol:

                if self.opcion_minimo == "Mínimo":
                    if f2 < f1:  # Buscando un mínimo
                        self.xu = x1
                    else:
                        self.xl = x2
                else:
                    if f2 > f1:  # Buscando un mínimo
                        self.xu = x1
                    else:
                        self.xl = x2

                a = invAureo * (self.xu - self.xl)
                b = invAureo * invAureo * (self.xu - self.xl)
                x1 = self.xl + a
                x2 = self.xl + b
                d = invAureo * (self.xu - self.xl)
                f1 = self.funcion.subs(self.x, x1).evalf()
                f2 = self.funcion.subs(self.x, x2).evalf()
                error = abs(x2 - x1)
                self.errores.append(error)
                self.iteraciones.append(i)
                self.resultados.append((i, self.xl, self.xu, d, x1, x2, f1, f2, error))
                i += 1

            if self.opcion_minimo == "Mínimo":
                self.datos = [("Iter", "xl", "xu", "d", "x1", "x2", "f1", "f2", "Error"),
                              f"El mínimo se encuentra en x1 o x2 = {x1}"]
            else:
                self.datos = [("Iter", "xl", "xu", "d", "x1", "x2", "f1", "f2", "Error"),
                              f"El máximo se encuentra en x1 o x2 = {x1}"]

            return self.resultados, self.iteraciones, self.errores, x1 if f1 < f2 else x2, error, self.datos
        except sp.SympifyError:
            raise ValueError("La función ingresada no es válida. Asegúrate de usar la sintaxis correcta.")
        except Exception as e:
            raise RuntimeError(f"Error inesperado: {str(e)}")
