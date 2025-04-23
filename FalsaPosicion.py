import sympy as sp

class FalsaPosicion:
    def __init__(self, funcion_str, xl, xu, iter_max, tol):
        self.funcion_str = funcion_str
        self.xl = xl
        self.xu = xu
        self.iter_max = iter_max
        self.tol = tol
        self.errores = []
        self.iteraciones = []
        self.resultados = []
        self.datos = []
        self.x = sp.symbols('x')
        self.funcion = sp.sympify(funcion_str)

    def calcular(self):
        try:
            fl = self.funcion.subs(self.x, self.xl).evalf()
            fu = self.funcion.subs(self.x, self.xu).evalf()

            if fl * fu > 0:
                raise ValueError("La función no cambia de signo en los intervalos dados.")

            xr = self.xu - ((fu * (self.xl - self.xu)) / (fl - fu))
            fr = self.funcion.subs(self.x, xr).evalf()
            error = abs(self.xu - xr)

            self.resultados.append((0, self.xu, self.xl, xr, fu, fl, fr, fl * fr, error))
            self.errores.append(error)
            self.iteraciones.append(0)

            i = 1
            while i <= self.iter_max and error > self.tol:
                fr = self.funcion.subs(self.x, xr).evalf()

                if fl * fr < 0:
                    self.xu = xr
                elif fu * fr < 0:
                    self.xl = xr
                elif fr == 0:
                    break  # Se encontró la raíz exacta

                fl = self.funcion.subs(self.x, self.xl).evalf()
                fu = self.funcion.subs(self.x, self.xu).evalf()
                xr = self.xu - ((fu * (self.xl - self.xu)) / (fl - fu))
                error = abs(self.xu - xr)

                self.errores.append(error)
                self.iteraciones.append(i)
                self.resultados.append((i, self.xu, self.xl, xr, fu, fl, fr, fl * fr, error))

                i += 1

            self.datos = [("Iter", "xu", "xl", "xr", "fu", "fl", "fr", "fl*fr", "Error"),
                          f"La raíz se encuentra en xr = {xr}"]

            return self.resultados, self.iteraciones, self.errores, xr, error, self.datos
        except sp.SympifyError:
            raise ValueError("La función ingresada no es válida.")
        except Exception as e:
            raise RuntimeError(f"Error inesperado: {str(e)}")
