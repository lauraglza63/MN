import sympy
from sympy import Abs
from sympy.abc import x
# los intervalos tienen q ser con numeros con comas o me da error sympy

FUNCTION= sympy.sympify('sin(x)-ln(x)')
ERROR= 10**-10
LIM=3

# en la primera iteracion de regula falsa no hay error
def regula_falsa(a, b):
    
    X_anterior= 10**6
    Error= Abs(X_anterior)
    i=0
    while Error >= ERROR and i<LIM:
        fa=FUNCTION.subs(x,a)
        fb=FUNCTION.subs(x,b)
        Xo=(b-a)/(fb-fa)*fa
        Xo=a-Xo
        Error= Abs(X_anterior-Xo)
        d={'a':a, 'b': b, 'fa': fa, 'fb':fb, 'Aproximacion': Xo,'error': Error}
        print(d)
        if FUNCTION.subs(x,Xo)==0:
            return Xo
        elif FUNCTION.subs(x,Xo)*FUNCTION.subs(x,a)<0:
            b=Xo
        else:
            a=Xo
        X_anterior=Xo
        i+=1

regula_falsa(2.0, 2.5)
