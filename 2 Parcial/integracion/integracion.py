import sympy
import math

# los intervalos tienen q ser con numeros con comas o me da error sympy

x= sympy.Symbol('x')
f= sympy.sin(x)
LIM=10

def trapecios( a: float, b: float, n: int) -> float:
    h = (b - a) / n
    print(f"h es b-a/n = {h}")
    result: list[float] = []
    for i in range(0, n + 1):
        if i == 0 or i == n:
            result.append(f.subs(x,h * i + a) / 2)
        else:
            result.append(f.subs(x,h * i + a))
    print(f"result = h({result})")
    suma = sum(result)
    final = h * suma
    print(f"result = {final}")
    #poner limite manual
    if n == LIM:
        derivada = f.diff()
        truncmiento = -(derivada.subs(x, b) - derivada.subs(x, a)) / 12 * h**2
        print(f"error truncamiento asintotico= 0 <= R <= {truncmiento}")
        resultato_iter_anterior = trapecios(a, b, int(n / 2))
        doble_calculo = (final - resultato_iter_anterior) / 3
        print(f"error doble calculo = {doble_calculo}")
    return final


def simpson( a: float, b: float, n: int) -> float:
    h = (b - a) / n
    print(f"h es b-a/n = {h}")
    result: list[float] = []
    for i in range(0, n + 1):
        if i == 0 or i == n:
            result.append(f.subs(x,h * i + a))
        elif i % 2 == 0:
            result.append(f.subs(x,h * i + a)*2)
        else:
            result.append(f.subs(x,h * i + a) * 4)

    print(f"result = h({result})")
    suma = sum(result)
    final = h / 3 * suma
    print(f"result = {final}")
    #poner limite manual
    if n == LIM:
        derivada = f.diff().diff().diff()
        truncmiento = -(derivada.subs(x, b) - derivada.subs(x, a)) / 180 * h*4
        print(f"error truncamiento asintotico= 0 <= R <= {truncmiento}")
        resultato_iter_anterior = trapecios(a, b, int(n / 2))
        doble_calculo = (final - resultato_iter_anterior) / 15
        print(f"error doble calculo = {doble_calculo}")
    return final


#trapecios(0, math.pi, 10)
simpson(0,math.pi, 10)