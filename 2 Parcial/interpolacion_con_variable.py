import sympy
from sympy.functions import factorial, Abs

x= sympy.Symbol('x')

num_list=[[4.9669,5.0082,5.0495],[100.0065,100.0004,100.0149]]

def interpolacion_X():
    for i in range(len(num_list[0])):
        R=0
        R+= (x**2-num_list[0][i-1]*x-num_list[0][i-2]*x-num_list[0][i-1]*num_list[0][i-2])*num_list[1][i]
        # print(R)
    return R


print(interpolacion_X())