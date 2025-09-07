# for é usando para criar laços de repetições
# principalmente quando o numero de repetições pode ser estabelecido

#for i in range(10):
#    print(i)

#for i in range(1, 11): #vai de 1 ate 10
#    print(i)

# for i in range(1, 100, 7): #vai de 1 ate 100 de 7 em 7
#     print(i)

# nums = [2, 4, 5, 6]

# for n in nums:
#    print(n, end=' ')

# for n in nums:
#    print(n)

texto = 'Python é muito massa!'

# age sobre uma string letra por letra
for letra in texto:
    print(letra, end=' ')

produto = {
    'nome': 'Caneta',
    'preco': 8.80,
    'desc': 0.5
}

# age sobre as chaves de um dicionario
for atrib in produto:
    print(atrib, '==>', produto[atrib])
# .items() retorna chave e valor em cada iteração
for atrib, valor in produto.items():
    print(atrib, '==>', valor)
# .values() retorna apenas os valores
for valor in produto.values():
    print(valor, end=' ')
# .keys() retorna apenas as chaves
for atrib in produto.keys():
    print(valor, end=' ')