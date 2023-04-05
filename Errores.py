import sympy
from sympy.functions import Abs

def error(X, Xa):
    return X-Xa

def errorAbs(X, Xa):
    return Abs(error(X, Xa))

def errorRel(EAbs, X):
    return EAbs/Abs(X)

def conseguirErrorAbsMax(exponente):
    return 0.5*(10**exponente)

def ultimaCifraExacta(error):
    result=0
    if error>0.5:
        while error>0.5:
            error/=10
            result+=1
    else:
        while error*10 <= 0.5:
            error*=10
            result-=1
    return result


print(ultimaCifraExacta(0.00078))
print(errorRel(7, 8.5))