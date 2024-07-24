import sympy as sp
import math
import matplotlib.pyplot as plt
import numpy as np
import dataframe_image as dfi
import pandas as pd
x = sp.symbols('x')
def adicionar_dados(df,n, x_n, f_xn, fd_xn, erro, arquivo='tabela.csv'):

    novo_dado = pd.Series({
        'n': n,
        'x_n': x_n,
        'f(x_n)': f_xn,
        'f\'(x_n)': fd_xn,
        'erro': erro
    })

    df = pd.concat([df, novo_dado.to_frame().T], ignore_index=True)

    
    df.to_csv(arquivo, index=False)
    return df
def iteracoes(a,b,e):
    x = math.log(b-a,10) - math.log(e,10)/math.log(2,10)
    return round(x-1)

def m_newton(f,derivada,limite,xi,e):
    df = pd.DataFrame(columns=['n', 'x_n', 'f(x_n)', 'f\'(x_n)', "erro"])
    n = 0 
    x_ant = 0
    while(n <= limite):
        fxi = f.subs(x,xi)
        fdxi = derivada.subs(x,xi)
        df = adicionar_dados(df,n,xi,fxi,fdxi,xi - x_ant)
        n = n + 1
        if(fxi == 0 or abs(xi - x_ant) < e ):
            return [n,xi]
        x_ant = xi
        xi = x_ant - fxi/fdxi
        
    return [xi,n]
expr = x**4 -4*x**2+7*x-11
derivada = sp.diff(expr, x)
f = sp.lambdify(x, expr, 'numpy')
x_vals = np.linspace(-10,10)
y_vals = f(x_vals)
plt.plot(x_vals, y_vals, label="f(x)")
plt.grid(True)
plt.show()
xi = float(input("valor inicial "))
n = float(input("limite interações "))
e = float(input("erro de toleracia "))


resultado = m_newton(expr,derivada,n,xi,e)

df = pd.read_csv("tabela.csv")
df.dfi.export('/df.png')
print("interações = ",resultado[0])
print("a raiz é ",resultado[1])