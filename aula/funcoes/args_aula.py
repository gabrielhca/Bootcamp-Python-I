# *args agrupa argumentos posicionais em uma tupla
def soma(*nums):
    total = 0
    for n in nums:
        total += n
    return total

# **kwargs agrupa argumentos nomeados em um dicionario
def resultado_final(**kwargs):
    status = 'aprovado(a)' if kwargs['nota'] >= 7 else 'reprovado(a)'
    return f'{kwargs["nome"]} foi {status}'