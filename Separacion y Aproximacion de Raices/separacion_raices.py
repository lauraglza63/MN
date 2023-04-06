import sympy

x= sympy.Symbol('x')
FUNCTION1= sympy.sin(x)-sympy.log(x)
FUNCTION2= x**2

def formulaLarange(B, Ao, k):
    return 1+ sympy.root((B/Ao), k)

def evaluar_funcion(xo):
    return FUNCTION1.subs(x,xo)

def bolzano(a,b):
    fa=FUNCTION1.subs(x,a)
    fb=FUNCTION1.subs(x,b)
    d={'fa':fa, 'fb':fb, 'cumple_bolzano': fa*fb<0}
    print(d)

print(formulaLarange(4, 1, 1))

# print(evaluar_funcion(-0.5))

bolzano(2, 2.5)