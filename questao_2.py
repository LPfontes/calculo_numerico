import sympy as sp
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
x = sp.symbols('x')
def adicionar_dados(df,n, a, b, x_n1, f_a, f_b, f_x_n1,erro, arquivo='tabela.csv'):

    novo_dado = pd.Series({
        'n': n,
        'a': a,
        'b': b,
        'Xn': x_n1,
        'f(a)': f_a,
        'f(b)': f_b,
        'f(Xn)': f_x_n1,
        '(b-a)/2':erro
    })

    df = pd.concat([df, novo_dado.to_frame().T], ignore_index=True)

    
    df.to_csv(arquivo, index=False)
    return df
def iteracoes(a,b,e):
    x = math.log(b-a,10) - math.log(e,10)/math.log(2,10)
    return round(x-1)

def Bisseccao(f,a,b,e):
    df = pd.DataFrame(columns=['n', 'a', 'b', 'Xn', 'f(a)', 'f(b)', 'f(Xn)','(b-a)/2'])
    limite = iteracoes(a,b,e)
    n = 0 
    while(n <= limite):

        xi = (a+b)/2
        fxi = f.subs(x, xi)
        fa = f.subs(x, a)
        fb = f.subs(x, b)
        df = adicionar_dados(df,n,a,b,xi,fa,fb,fxi,abs(b - a)/2)
        n = n + 1
        if((fxi == 0) or abs(b - a)/2 < e):
            return xi
        elif(fa*fxi< 0):
            b = xi
        else:
            a = xi
    return xi
S = 32  # m
L = 30  # me
alpha = 0.10  # kgf/m                                                                                                                                                                                                   
expr = (2 * x / alpha) * sp.sinh((alpha * L) / (2 * x)) - S

f = sp.lambdify(x, expr, 'numpy')
x_vals = np.linspace(-10,10)
y_vals = f(x_vals)
plt.plot(x_vals, y_vals, label="f(x)")
plt.grid(True)
plt.show()
a = 2
b = 3
e = 0.01
n = iteracoes(a,b,e)
print(n)
if(expr.subs(x, a)*expr.subs(x, b)< 0):
    raiz = Bisseccao(expr,a,b,e)
    print("a raiz é ",raiz)    
else:
    print("intervalo invalido")

print("a raiz é ",raiz)