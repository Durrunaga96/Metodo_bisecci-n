#importando modulos:

%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#implementando funciones:

def Pendiente(x1, x2, f):
    if (x1 == x2):
        return 'Ingrese dos puntos distintos'
    else:
        m = (f(x2) - f(x1))/(x2 - x1)
        return m
 
 def CorteEjeX(x1, x2, f):
    m = Pendiente(x1, x2, f)
    x = x1 - (1/m)*f(x1)
    return x
 
 #Implementando el método de la secante:
 
 def MetodoSecante(x0, x1, Tol, f):
    sol = [x1]

    i = 0
    while(True):
        x = CorteEjeX(x0, x1, f)
        sol = sol + [x]
        x0 = x1
        x1 = x
        if(abs(sol[i+1] - sol[i]) <= Tol):
            break

        i = i + 1
    sol_resp = sol
    for i in range(0, len(sol_resp)):
        sol_resp[i] = str(sol_resp[i])
    return pd.DataFrame(sol_resp, columns=[r'$x_i$'])
