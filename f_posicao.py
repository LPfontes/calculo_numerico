import sympy as sp
import math
import matplotlib.pyplot as plt
import numpy as np
import re
import pandas as pd
x = sp.symbols('x')
def adicionar_dados(df,n, a, b, x_n1, f_a, f_b, f_x_n1, arquivo='tabela.csv'):

    novo_dado = pd.Series({
        'n': n,
        'a': a,
        'b': b,
        'x_{n+1}': x_n1,
        'f(a)': f_a,
        'f(b)': f_b,
        'f(x_{n+1})': f_x_n1
    })

    df = pd.concat([df, novo_dado.to_frame().T], ignore_index=True)

    
    df.to_csv(arquivo, index=False)
    return df
def iteracoes(a,b,e):
    x = math.log(b-a,10) - math.log(e,10)/math.log(2,10)
    return round(x-1)

def falsa_posiccao(f,a,b,e):
    df = pd.DataFrame(columns=['n', 'a', 'b', 'x_{n+1}', 'f(a)', 'f(b)', 'f(x_{n+1})'])
    limite = iteracoes(a,b,e)
    n = 0
    x_ant = 0 
    while(n <= limite):
        fa = f.subs(x, a)
        fb = f.subs(x, b)
        xi = (a*fb-b*fa)/(fb -fa)
        fxi = f.subs(x, xi)
        df =adicionar_dados(df,n,a,b,(a+b)/2, fa,fb,fxi)
        n = n + 1
        if(fxi == 0 or abs(xi- x_ant) < e ):
            return [n,xi]
        elif(fa*fxi< 0):
            x_ant = xi
            b = xi
        else:
            x_ant = xi
            a = xi
    return [xi,n]
expr = x**3 + sp.cos(x)

f = sp.lambdify(x, expr, 'numpy')
x_vals = np.linspace(-10,10)
y_vals = f(x_vals)
plt.plot(x_vals, y_vals, label="f(x)")
plt.grid(True)
plt.show()
a = float(input("inicio do intervalo "))
b = float(input("final do intervalo "))
e = float(input("erro de toleracia "))
n = iteracoes(a,b,e)
if(expr.subs(x, a)*expr.subs(x, b)< 0):
    resultado = falsa_posiccao(expr,a,b,e)
else:
    print("intervalo invalido")
df = pd.read_csv("tabela.csv")
print("interações = ",resultado[0])
print("a raiz é ",resultado[1])