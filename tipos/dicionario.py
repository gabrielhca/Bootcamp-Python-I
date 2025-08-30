# dicionarios são coleções não ordenadas de pares 'chave: valor'
aluno = {
    'nome' : 'Pedro Henrique',
    'nota' : 9.2,
    'ativo' : True
}

print(type(aluno))
# acessa o valor pela chave
print(aluno['nome'])
print(aluno['nota'])
print(aluno['ativo'])
# retorna a quantidade de pares
print(len(aluno))