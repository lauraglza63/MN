import sympy
from sympy import simplify

# los intervalos tienen q ser con numeros con comas o me da error sympy

x= sympy.Symbol('x')
f= x**2*(x-4)**2

def biseccion( a: float, b: float, error: float, max: bool):
    l = b - a
    d = 0.1 * error
    print(f"a,    b,     l,     x1,     y1,    y2")
    while l >= error:
        x1 = (a + b) / 2 - d / 2
        x2 = (a + b) / 2 + d / 2
        y1 = f.subs(x,x1)
        y2 = f.subs(x,x2)
        dic={'a':a, 'b':b, 'l':l, 'x1':x1, 'x2':x2, 'y1':y1,'y2': y2}
        print(dic)
        if max:
            aux = y1
            y1 = y2
            y2 = aux
        if y1 > y2:
            a = x1
        elif y1 < y2:
            b = x2
        else:
            a=x1
            b=x2
            break
        l = b - a
    print(f"El extremo se encuentra en el intervalo [{a}, {b}], l = {l}")
    medio = (a + b) / 2
    print(f"medio {medio}")
    ya = f.subs(x,a)
    ym = f.subs(x,medio)
    yb = f.subs(x,b)
    print(f"las y son: {ya}, {ym}, {yb}")
    #interpolacion_lagrange([a, medio, b], [ya, ym, yb], a)


def seccion_de_oro( a: float, b: float, error: float, max: bool):
    factor = 0.382
    l = b - a
    x1 = a + factor * l
    x2 = b - factor * l
    y1 = f.subs(x,x1)
    y2 = f.subs(x,x2)
    while l >= error:
        dic={'a':a, 'b':b, 'l':l, 'x1':x1, 'x2':x2, 'y1':y1,'y2': y2}
        print(dic)
        comp = False
        if (max and y1 < y2) or (not max and y1 > y2):
            comp = True
        if comp:
            a = x1
            x1 = x2
            y1 = y2
            l = b - a
            x2 = b - factor * l
            y2 = f.subs(x,x2)
        else:
            b = x2
            x2 = x1
            y2 = y1
            l = b - a
            x1 = a + factor * l
            y1 = f.subs(x,x1)
    print(f"El extremo se encuentra en el intervalo [{a}, {b}], l = {l}")
    medio = (a + b) / 2
    print(f"medio {medio}")
    ya = f.subs(x,a)
    ym = f.subs(x,medio)
    yb = f.subs(x,b)
    print(f"las y son: {ya}, {ym}, {yb}")
    #interpolacion_lagrange([a, medio, b], [ya, ym, yb], a)


def interpolacion_lagrange(x_list: list[float], y_list: list[float], xp: float):
    polinomios: list[Function] = []
    for i in range(len(x_list)):
        numerador = ""
        denominador = ""
        for j in range(len(x_list)):
            if i != j:
                numerador += f"(x - {x_list[j]}) * "
                denominador += f"({x_list[i]} - {x_list[j]}) * "
        numerador = numerador[:len(numerador) - 3]
        denominador = denominador[:len(denominador) - 3]
        polinomios.append(simplify(f"({numerador}) / ({denominador})"))

    yp: Expr = simplify("0")
    for i, f in enumerate(polinomios):
        yp = simplify(yp + (f * y_list[i]))
    print(yp)
    print(yp.subs(x, xp))


#biseccion(3, 5, 0.1, False)
seccion_de_oro(3, 5, 0.1, False)