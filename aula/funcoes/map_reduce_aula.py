from functools import reduce

# map() aplica uma função a cada item de uma sequencia
def somar_nota(delta):
    def calc(nota):
        return nota + delta
    return calc


notas = [6.4, 7.2, 5.8, 8.4]
notas_finais_1 = map(somar_nota(1.5), notas)
notas_finais_2 = map(somar_nota(1.6), notas)

print(list(notas_finais_1))
print(list(notas_finais_2))

# reduce() acumula os valores
def somar(a, b):
    return a + b

total = reduce(somar, notas, 0)
print(total)

#for i, nota in enumerate(notas):
#    notas[i] = nota + 1.5

#for i in range(len(notas)):
#    notas[i] = notas[i] + 1.5
