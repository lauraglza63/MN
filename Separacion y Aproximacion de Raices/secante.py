import sympy
from sympy.functions import Abs

# los numeros a pasar al evaluar las funciones tienen q ser numeros con comas o me da error sympy

x= sympy.Symbol('x')
FUNCTION= sympy.sin(x)-sympy.log(x)
ERROR= 0.5*10**-4
LIM=20

# en la primera iteracion de la secante no hay error
def secante(Xa, Xb):
    Ya = FUNCTION.subs(x,Xa)
    Yb = FUNCTION.subs(x,Xb)
    Error= Abs(Xb-Xa)
    i=0
    while Error >= ERROR and i<LIM:
        Xc=Xb-(Xb-Xa)/(Yb-Ya)*Yb
        Error=Abs(Xc-Xb)
        # 'fa':Ya, 'fb': Yb,
        d={'Xa':Xa, 'Xb': Xb, 'Aproximacion': Xc,'error': Error}
        print(d)
        Yc=FUNCTION.subs(x,Xc)
        # if Yc ==0:
        #     return Xc
        Xa=Xb
        Ya=Yb
        Xb=Xc
        Yb= Yc
        i+=1

#para elegir Xa y Xb lo hago a traves del grafico, agrando y puntos mas cercanos
secante(2.22, 2.219)