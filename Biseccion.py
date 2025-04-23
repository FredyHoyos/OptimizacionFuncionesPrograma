import sympy as sp

class Biseccion:
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

            xr = (self.xu + self.xl) / 2
            error = abs(self.xl - self.xu) / 2
            fr = self.funcion.subs(self.x, xr).evalf()
            self.errores.append(error)
            self.iteraciones.append(0)
            self.resultados.append((0, self.xu, self.xl, xr, fu, fl, fr, fl * fr, error))
            i = 1
            while i <= self.iter_max and error > self.tol:
                fr = self.funcion.subs(self.x, xr).evalf()

                if fl * fr < 0:
                    self.xu = xr
                    #error = abs(self.xl + self.xu) / 2
                elif fl * fr > 0:
                    self.xl = xr
                    #error = abs(self.xl - self.xu) / 2
                else:
                    break

                fl = self.funcion.subs(self.x, self.xl).evalf()
                fu = self.funcion.subs(self.x, self.xu).evalf()
                xr = (self.xu + self.xl) / 2
                error = abs(self.xl - self.xu) / 2

                self.errores.append(error)
                self.iteraciones.append(i)
                self.resultados.append((i, self.xu, self.xl, xr, fu, fl, fr, fl * fr, error))


                i += 1

            self.datos = [("Iter", "xu", "xl", "xr", "fu", "fl", "fr", "fl*fr", "Error"),
                          f"La raiz se encuentra en xr = {xr}"]
            return self.resultados, self.iteraciones, self.errores, xr, error, self.datos
        except sp.SympifyError:
            raise ValueError("La función ingresada no es válida.")
        except Exception as e:
            raise RuntimeError(f"Error inesperado: {str(e)}")
