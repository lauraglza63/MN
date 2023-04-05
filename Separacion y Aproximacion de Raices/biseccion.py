import sympy

# los intervalos tienen q ser con numeros con comas o me da error sympy

x= sympy.Symbol('x')
FUNCTION= sympy.exp(-x)-sympy.log(x)
ERROR= 10**-100
LIM=5

def biseccion(a,b):
    Error= (b-a)/2
    i=0
    while Error >= ERROR and i<LIM:
        xa= (a+b)/2
        Error= (b-a)/2
        d={'a':a, 'b': b, 'Aproximacion': xa,'error': Error}
        print(d)
        if FUNCTION.subs(x,xa)==0:
            return xa
        elif FUNCTION.subs(x,xa)*FUNCTION.subs(x,a)<0:
            b=xa
        else:
            a=xa
        i+=1
        

biseccion( 1, 1.5)