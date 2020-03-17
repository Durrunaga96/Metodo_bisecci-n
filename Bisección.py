#importando modulos
import numpy as np
import pandas as pd

#implementando método de la bisección
def MetodoBiseccion(a, b, Tol,g):
    salida = True  
    FA = g(a)
    FB = g(b)
    p = (b + a)/2
    FP = g(p)
    Sol = [p]
    i=0
    while(True):
        if( FA*FP<0 ):
            b = p
            p = (a+b)/2
            FB = g(b)
            FP = g(p)
        elif(FB*FP<0):
            a = p
            p = (a + b)/2
            FA = g(a)
            FP = g(p)
        else:
            salida = False
            retorna= 'No se pude realizar el Método de la Biseccion'
        Sol = Sol+[p]
        if( abs(Sol[i+1] - Sol[i]) <= Tol ):
            ultimo = i+1
            break
        i = i+1
    if( salida == True ):
        sol_resp = Sol
        for i in range(0, len(sol_resp)):
            sol_resp[i] = str(sol_resp[i])
        datos1 = {r'$P_{i}$': sol_resp}
        return pd.DataFrame(datos1, columns=[r'$P_{i}$'])
               
                
    else:
        return retorna
