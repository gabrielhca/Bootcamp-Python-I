# tuplas são coleções ordenadas e imutaveis
nomes = ('Ana', 'Bia', 'Gui', 'Ana', 'Leo')

# 'in' checa se um elemento existe na tupla
print('Bia' in nomes) # return True

# assim como nas listas, podemos acessar elementos por indice
print(nomes[0])
# extrai apenas uma parte da tupla [começo:fim]
print(nomes[1:2])
print(nomes[1:3])
# -1 é o ultimo elemento
print(nomes[1:-1])
# do 2 ate o fim
print(nomes[2:])
# do inicio ate o penultimo
print(nomes[:-2])
print(len(nomes))

# tuplas d eum unico elmentos precisam de uma virgula no final
x = ('Bia',)
print(type(x))

print(type(nomes))
print(nomes)