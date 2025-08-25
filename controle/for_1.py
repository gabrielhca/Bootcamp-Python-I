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

for letra in texto:
    print(letra, end=' ')

produto = {
    'nome': 'Caneta',
    'preco': 8.80,
    'desc': 0.5
}

for atrib in produto:
    print(atrib, '==>', produto[atrib])

for atrib, valor in produto.items():
    print(atrib, '==>', valor)

for valor in produto.values():
    print(valor, end=' ')

for atrib in produto.keys():
    print(valor, end=' ')