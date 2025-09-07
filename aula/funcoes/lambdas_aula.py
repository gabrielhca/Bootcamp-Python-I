from functools import reduce

alunos = [
    {'nome': 'Ana', 'nota': 7.2},
    {'nome': 'Pedro', 'nota': 9.5},
    {'nome': 'Paulo', 'nota': 5.3},
    {'nome': 'Cintia', 'nota': 10.0},
    {'nome': 'Vanessa', 'nota': 6.2}
]

# lambda são funções anonimas (sem nome)  e concisas, inspiradas no calculo lambda
aluno_aprovado = lambda aluno: aluno['nota'] >= 7
# aluno_honra = lambda aluno: aluno['nota'] >= 9
obter_nota = lambda aluno: aluno['nota']
somar = lambda a, b: a + b

# filter() filtras os elementos
aluno_aprovados = filter(aluno_aprovado, alunos)
# map() mapeia os elementos
notas_alunos_aprovados = map(obter_nota, aluno_aprovados)
# reduce() acumula os valores
total =  reduce(somar, notas_alunos_aprovados, 0)

print(obter_nota(alunos[2]))

print(list(alunos))
print(list(notas_alunos_aprovados))

print(total)
# print(total / len(aluno_aprovados))