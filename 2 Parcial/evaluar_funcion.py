import sympy

# los intervalos tienen q ser con numeros con comas o me da error sympy

x= sympy.Symbol('x')
FUNCTION= 2*x**3-24*x**2+90*x

def evaluar_funcion(Xo):
    return FUNCTION.subs(x,Xo)

# sumar=0.1
# paso=0
# xo=3
# for i in range(10):
#     d={'iteracion': i, 'paso': paso, 'Xi': xo, 'Yi':evaluar_funcion(xo) }
#     print(d)
#     paso+=sumar
#     xo+=paso

print(evaluar_funcion(5.0082))
