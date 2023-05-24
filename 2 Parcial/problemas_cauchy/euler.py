import sympy

# los intervalos tienen q ser con numeros con comas o me da error sympy

x= sympy.Symbol('x')
y= sympy.Symbol('y')
FUNCTION= x/y

def euler(a,b,Yo,n):
    paso = (b - a) / n
    print(f"paso = {paso}")
    i=0
    dic={f'X{i}':a, f'Y{i}':Yo}
    print(dic)
    while True:
        i+=1
        eval_ant=FUNCTION.subs([(x,a),(y,Yo)])
        a=a+paso
        Yo=Yo+paso*eval_ant
        dic={f'X{i}':a, f'Y{i}':Yo, 'F(xn-1,yn-1)': eval_ant}
        print(dic)
        if a>=b:
            break

#se llama error por doble calculo
def error_euler(Yh,Y2h):
    error=Yh-Y2h
    print(error)
    return error

euler(1, 3, 2, 4)
