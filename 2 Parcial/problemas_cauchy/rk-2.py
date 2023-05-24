import sympy

# los intervalos tienen q ser con numeros con comas o me da error sympy

x= sympy.Symbol('x')
y= sympy.Symbol('y')
FUNCTION= x/y
ERROR= 10**-100
LIM=3

def rk_2(a,b,Yo,n):
    paso = (b - a) / n
    print(f"paso = {paso}")
    i=0
    dic={f'X{i}':a, f'Y{i}':Yo}
    print(dic)
    while True:
        i+=1
        Xn=a+paso
        eval_ant=FUNCTION.subs([(x,a),(y,Yo)])
        K1=paso*eval_ant
        eval_k2=FUNCTION.subs([(x,Xn),(y,Yo+K1)])
        K2=paso*eval_k2
        Yn=Yo+(K1+K2)/2
        dic={f'X{i}':Xn,'K1':K1,'K2':K2 ,f'Y{i}':Yn, 'F(xn-1,yn-1)': eval_ant,'F(para k2)': eval_k2}
        print(dic)

        #nuevos valores
        a=Xn
        Yo=Yn
        if a >= b:
            break

#se llama error por doble calculo
def error_rk_2(Yh,Y2h):
    error=(Yh-Y2h)/3
    print(error)
    return error

rk_2(1, 3, 2, 4)