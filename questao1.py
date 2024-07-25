import math


def func_gravidade(u, M0, g, c, t):
    # Calcula a função fornecida com os parâmetros específicos
    frac = M0 / (M0 - c * t)
    result = u * math.log(frac) + g * t - 100
    return result


def bisseccao(a, b, u, M0, g, c, tol, max_iter=1000):
    fa = func_gravidade(u, M0, g, c, a)
    fb = func_gravidade(u, M0, g, c, b)

    if fa * fb > 0:
        print("A função tem o mesmo sinal em ambos os extremos do intervalo.")
        return None

    x_old = a
    for i in range(max_iter):
        x = (a + b) / 2  # Calcula o ponto médio
        fx = func_gravidade(u, M0, g, c, x)
        # Evita divisão por zero
        erro_relativo = abs(x - x_old) / abs(x) if x != 0 else float('inf')

        # Imprime o erro relativo a cada iteração
        print(
            f"Iteração {i+1}: x = {x:.4f}, Erro Relativo = {erro_relativo:.10f}")

        # Verifica o critério de parada
        if erro_relativo < tol:
            return x

        # Atualiza o intervalo
        if fa * fx < 0:
            b = x
            fb = fx
        else:
            a = x
            fa = fx

        x_old = x  # Atualiza o valor anterior para verificar o erro na próxima iteração

    print("O método não convergiu após o máximo de iterações.")
    return None


# Parâmetros dados
u = 200
M0 = 1600
g = 9.8
c = 27
intervalo = [6, 8]
tolerancia = 0.008

# Executa o método da bissecção
resultado = bisseccao(intervalo[0], intervalo[1], u, M0, g, c, tolerancia)
if resultado is not None:
    print(f"A raiz encontrada é t = {resultado:.4f}")
else:
    print("Não foi possível encontrar uma raiz no intervalo dado.")
