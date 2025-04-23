import sympy as sp

class MetodoNewton:
    def __init__(self, funcion_str, xi, iter_max, tol):
        self.funcion_str = funcion_str
        self.xi = xi
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
            fx = float(self.funcion.subs(self.x, self.xi).evalf())
            dfx_expr = sp.diff(self.funcion, self.x)  # Mantén la derivada simbólica
            dfx = float(dfx_expr.subs(self.x, self.xi).evalf())
            xi_new = self.xi - (fx / dfx)
            error = abs(xi_new - self.xi)

            self.iteraciones.append(0)
            self.errores.append(error)
            self.resultados.append((0, self.xi, fx, dfx, error))
            self.xi = xi_new
            i = 1
            while i <= self.iter_max and error > self.tol:
                if dfx == 0:
                    raise ValueError("Derivada cero, no se puede continuar.")

                fx = float(self.funcion.subs(self.x, self.xi).evalf())
                dfx = float(dfx_expr.subs(self.x, self.xi).evalf())
                xi_new = self.xi - (fx / dfx)
                error = abs(xi_new - self.xi)
                self.resultados.append((i, self.xi, fx, dfx, error))
                self.iteraciones.append(i)
                self.errores.append(error)
                self.xi = xi_new
                i += 1

            self.datos = [("Iter", "x", "f(x)", "f'(x)", "Error"), f"La raíz se encuentra en x = {self.xi}"]
            return self.resultados, self.iteraciones, self.errores, self.xi, error, self.datos
        except sp.SympifyError:
            raise ValueError("La función ingresada no es válida.")
        except Exception as e:
            raise RuntimeError(f"Error inesperado: {str(e)}")
