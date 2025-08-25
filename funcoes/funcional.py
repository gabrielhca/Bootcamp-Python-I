def soma(a, b):
    return a + b

somar = soma
print(somar(3, 4))

def sub(a, b):
    return a - b


def operacao_aritmetica(fn, op1, op2):
    return fn(op1, op2)

resultado = operacao_aritmetica(soma, 13, 48)
print(resultado)

resultado = operacao_aritmetica(sub, 13, 48)
print(resultado)

# processamento parcial e otimização de velocidade
def soma_parcial(a):
    # processamento pesado 1 -10s
    # processamento pesado 2 -10s
    # processamento pesado 3 -40s
    def concluir_soma(b):
        return a + b # 10s
    return concluir_soma

resultado_final = soma_parcial(10)(12)
print(resultado_final)