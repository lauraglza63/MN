import sympy
from sympy import Abs

# M=[[columna1],[columna2]]
MATRIZ_M=[[0,-1/10,0],[-1/10, 0, -1/10],[0, -1/10, 0]]
MATRIZ_N=[11/10, 12/10, 11/10]
LIM=1
LATITUD= 10**-100

def seide():
    matiz_x=[0,0,0]
    beta=calcular_beta()
    for i in range(LIM):
        n=len(MATRIZ_M)
        matriz_anterior=matiz_x[:]
        for j in range(n):
            matiz_x[j]=MATRIZ_M[j][0]*matiz_x[0]+ MATRIZ_M[j][1]*matiz_x[1]+ MATRIZ_M[j][2]*matiz_x[2]+MATRIZ_N[j]
            print(matiz_x)
        
        print(f'Iteracion {i+1}: {matiz_x}')
        
        error= error_seide(matiz_x, matriz_anterior, beta)
        print(f'Error absoluto:  {error}')
        if error<LATITUD:
            break

def error_seide(matriz_1, matriz_2, beta):
    temp_list=[]
    for i in range(len(matriz_1)):
        temp_list.append(matriz_1[i]-matriz_2[i])
    maximo= float(max(temp_list))
    error= beta/(1-beta)*maximo
    return Abs(error)


def calcular_beta():
    beta_list=[]
    q= q_list()
    p=p_list()
    for i in range(len(q)):
        beta_list.append(q[i]/(1-p[i]))
    
    print(f'Betas: {beta_list}')
    maximo=float(max(beta_list))
    print(f'El valor maximo es: {maximo}')
    return maximo


def q_list():
    q_list=[]
    n=len(MATRIZ_M)
    for i in range(n):
        num=0
        j=n-i-1
        while j>=0:
            num+=Abs(MATRIZ_M[i][j])
            j-=1
        q_list.append(num)
    # print(f'q_list: {q_list}')
    return q_list

def p_list():
    p_list=[]
    n=len(MATRIZ_M)
    for i in range(n):
        num=0
        for j in range(i+1):
            num+=Abs(MATRIZ_M[i][j])
        p_list.append(num)
    # print(f'p_list: {p_list}')
    return p_list

seide()
# calcular_beta()

