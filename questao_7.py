def taxa_juros(financiamento=2499, parcelas=249, meses=12, erro=1e-7):

    def expressao_financeira(juros):
        return parcelas - (financiamento * juros) / (1 - (1 + juros)**-meses)

    def derivada_expressao(juros):
        numerator = financiamento * (1 - (1 + juros)**-meses) - financiamento * juros * meses * (1 + juros)**-(meses + 1)
        denominator = (1 - (1 + juros)**-meses)**2
        return numerator / denominator

    def metodo_newton(funcao, derivada, x0, max_iter=100):
        x = x0
        for _ in range(max_iter):
            fx = funcao(x)
            fdx = derivada(x)
            x_new = x - fx / fdx
            if abs(x_new - x) < erro:
                return x_new
            
            x = x_new

    def margem_juros_incial():
        menor, maior = 0.0001, 1.0

        while maior - menor > erro:
            media = (maior + menor)/2
            if expressao_financeira(media) * derivada_expressao(menor) < 0:
                maior = media
            else:
                menor = media
        return (maior + menor)/2

    chute_inicial = margem_juros_incial()
    taxa_juros = metodo_newton(expressao_financeira, derivada_expressao, chute_inicial)

    return taxa_juros * 100

juros = taxa_juros()

if juros is not None:
    print(f"A taxa de juros mensal é: {juros:.7f}%")
else:
    print("Não foi possível calcular a taxa de juros.")
