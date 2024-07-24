import math
S = 32  # meters
L = 30  # meters
alpha = 0.10  # kgf/m
def f(T):
    return (2 * T / alpha) * math.sinh((alpha * L) / (2 * T)) - S
print(f(2.3984375))