import sympy as sp
import math
import matplotlib.pyplot as plt
import numpy as np
import dataframe_image as dfi
import pandas as pd
x = sp.symbols('x')
def adicionar_dados(df,n, x_n, f_xn, f_xn_1,f_xn_2,x_ant_1,x_ant, erro, arquivo='tabela.csv'):

    novo_dado = pd.Series({
        'n': n,
        'Xn-1':x_ant_1,
        'Xn': x_ant,
        'Xn+1':x_n,
        'f(Xn-1)': f_xn,
        'f(Xn)': f_xn_1,
        'f(Xn+1)':f_xn_2,
        'erro': erro
    })

    df = pd.concat([df, novo_dado.to_frame().T], ignore_index=True)

    
    df.to_csv(arquivo, index=False)
    return df
def iteracoes(a,b,e):
    x = math.log(b-a,10) - math.log(e,10)/math.log(2,10)
    return round(x-1)

def m_secante(f,derivada,limite,x_0,x_1,e):
    df = pd.DataFrame(columns=['n', 'Xn-1', 'Xn',"Xn+1", 'f(Xn-1)','f(Xn)','f(Xn+1)', "erro"])
    n = 0 
    x_ant_1 = x_0
    x_ant = x_1
    xi = x_1
    fxi_1 = f.subs(x,x_ant_1)
    while(n <= limite):
        fxi = f.subs(x,xi)
        n = n + 1
        xi = float(x_ant_1*fxi-xi*fxi_1)/(fxi-fxi_1)
        df = adicionar_dados(df,n, xi, fxi_1,fxi ,f.subs(x,xi),x_ant_1,x_ant, xi - x_ant)
        x_ant_1 = x_ant
        fxi_1 = f.subs(x,x_ant_1)
        x_ant = xi

        if(fxi == 0 or abs(x_ant - x_ant_1) < e ):
            return [n,xi]
        
    return [xi,n]
expr = x**3 -9*x+3
derivada = sp.diff(expr, x)
f = sp.lambdify(x, expr, 'numpy')
x_vals = np.linspace(-10,10)
y_vals = f(x_vals)
plt.plot(x_vals, y_vals, label="f(x)")
plt.grid(True)
plt.show()
#x_0 = float(input("1 valor inicial "))
#x_1 = float(input("2 valor inicial "))
#n = float(input("limite interações "))
#e = float(input("erro de toleracia "))
x_0 = 0
x_1 = 1
e = 0.001
n= 6
resultado = m_secante(expr,derivada,n,x_0,x_1,e)

df = pd.read_csv("tabela.csv")
print("interações = ",resultado[0])
print("a raiz é ",resultado[1])