# exemplos de loops aninhados
pessoas = ['Gui', 'Rebeca']
adjs = ['Sapeca', 'Inteligente']

for p in pessoas:
    for a in adjs:
        print(f'{p} é {a}!')
# 'pass' não faz nada, é util para preencher blocos vazios
for i in [1, 2, 3]:
    pass
# 'continue' pula para a proxima iteração
for i in range(1, 11):
    if i % 2 == 1:
        continue
    print(i)
# 'break' interrompe o loop
for i in range(1,11):
    if i == 5:
        break
    print(i)

print('Fim')