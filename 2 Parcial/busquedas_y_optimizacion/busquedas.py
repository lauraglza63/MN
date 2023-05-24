import sympy

# los intervalos tienen q ser con numeros con comas o me da error sympy

x= sympy.Symbol('x')
f= sympy.sin(x)

def busqueda_secuencial(x0: float, paso: float, maximo: bool = True):
    x1 = x0
    x2 = x1 + paso
    x3 = x2 + paso
    y1 = f.subs(x,x1)
    y2 = f.subs(x,x2)
    y3 = f.subs(x,x3)
    print("x1,   x2,    x3,    y1,    y2,    y3")
    i=1
    while True:
        dic={'it':i, 'x1':x1, 'x2': x2, 'x3': x3, 'y1': y1, 'y2': y2, 'y3': y3}
        print(dic)
        if maximo:
            if y3 < y2:
                break
        elif y3 > y2:
            break
        x1 = x2
        x2 = x3
        x3 = x2 + paso
        y1 = y2
        y2 = y3
        y3 = f.subs(x,x3)
        i+=1
    print(f"El extremo se encuentra en el intervalo [{x1}, {x3}]")





def busqueda_secuencial_acelerada(x0: float, paso: float, maximo: bool = True):
    x1 = x0
    x2 = x1 + paso
    paso *= 2
    x3 = x2 + paso
    y1 = f.subs(x,x1)
    y2 = f.subs(x,x2)
    y3 = f.subs(x,x3)
    print("x1,   x2,    x3,    y1,    y2,    y3")
    i=1
    while True:
        dic={'it':i, 'x1':x1, 'x2': x2, 'x3': x3, 'y1': y1, 'y2': y2, 'y3': y3}
        print(dic)
        if maximo:
            if y3 < y2:
                break
        elif y3 > y2:
            break
        paso *= 2
        x1 = x2
        x2 = x3
        x3 = x2 + paso
        y1 = y2
        y2 = y3
        y3 = f.subs(x,x3)
        i+=1
    print(f"El extremo se encuentra en el intervalo [{x1}, {x3}]")

#busqueda_secuencial_acelerada(3.0, 0.1, False)
busqueda_secuencial(0.0, 0.1, True)