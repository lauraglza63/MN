import sympy

# los intervalos tienen q ser con numeros con comas o me da error sympy

x= sympy.Symbol('x')
y= sympy.Symbol('y')
FUNCTION= -2*x*y

def rk_4(a, b, Yo, n):
    paso = (b - a) / n
    print(f"paso = {paso}")
    i = 0
    dic = {f'X{i}': a, f'Y{i}': Yo}
    print(dic)
    while True:
        i+=1
        Xn = a + paso
        eval_ant = FUNCTION.subs([(x, a), (y, Yo)])
        K1 = paso * eval_ant
        eval_k2 = FUNCTION.subs([(x, a + paso / 2), (y, Yo + K1 / 2)])
        K2 = paso * eval_k2
        eval_k3 = FUNCTION.subs([(x, a + paso / 2), (y, Yo + K2 / 2)])
        K3 = paso * eval_k3
        eval_k4 = FUNCTION.subs([(x, a + paso), (y, Yo + K3)])
        K4 = paso * eval_k4
        Yn = Yo + (K1 + 2 * K2 + 2 * K3 + K4) / 6
        dic = {f'X{i}': Xn,
               'K1': K1,
               'K2': K2,
               'K3': K3,
               'K4': K4,
               f'Y{i}': Yn,
               'F(xn-1,yn-1)': eval_ant,
               'F(para k2)': eval_k2,
               'F(para k3)': eval_k3,
               'F(para k4)': eval_k4}
        print(dic)
        # nuevos valores
        a = Xn
        Yo = Yn
        if a >= b:
            break

#se llama error por doble calculo
def error_rk_4(Yh,Y2h):
    error=(Yh-Y2h)/15
    print(error)
    return error


rk_4(0, 2, 1, 4)