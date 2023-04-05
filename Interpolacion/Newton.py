import sympy

# numlist=[[x],[y]]
NUM_LIST=[[0,1,-1,2],[1,2.72,0.37,7.39]]
ERROR= 10**-10
# tamaño del polinomio, para hacer un polinomio de grado n necesito n+2 nodos
LIM= len(NUM_LIST[0])-2


def tabla_primerafila_dif():
    result=NUM_LIST[1][:]
    for i in range(1,len(NUM_LIST[0])):
        j=len(NUM_LIST[0])-1
        while(j>=i):
            result[j]= (result[j]-result[j-1])/(NUM_LIST[0][j]-NUM_LIST[0][j-i])
            j-=1
    return result

def inter_newton(x):
    dif_list=tabla_primerafila_dif()
    p=dif_list[0]
    producto= x-NUM_LIST[0][0]
    error= dif_list[1]*producto
    d={'p0': p, 'error': error}
    print(d)
    i=1
    while error>ERROR and i<=LIM:
        p=p+error
        producto*=x-NUM_LIST[0][i]
        i+=1
        error=dif_list[i]*producto
        d={f'p{i-1}': p, 'error': error}
        print(d)
    
    return p



print(tabla_primerafila_dif())

inter_newton(1.8)