import sympy
from sympy import Abs

# los intervalos tienen q ser con numeros con comas o me da error sympy

x= sympy.Symbol('x')
FUNCTION= x**2-sympy.cos(2*x)
ERROR= 10**-10
LIM=5

# en la primera iteracion de regula falsa no hay error
def regula_falsa(a, b):
    
    X_anterior= 10**6
    Error= Abs(X_anterior)
    i=0
    while Error >= ERROR and i<LIM:
        Xo= a-((b-a)/(FUNCTION.subs(x,b)-FUNCTION.subs(x,a)))*FUNCTION.subs(x,a)
        Error= Abs(X_anterior-Xo)
        d={'a':a, 'b': b, 'Aproximacion': Xo,'error': Error}
        print(d)
        if FUNCTION.subs(x,Xo)==0:
            return Xo
        elif FUNCTION.subs(x,Xo)*FUNCTION.subs(x,a)<0:
            b=Xo
        else:
            a=Xo
        X_anterior=Xo
        i+=1

regula_falsa(0.5, 1.0)
