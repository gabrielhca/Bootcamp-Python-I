# if/elif/else criam blocos de codigos que so são executados se uma condição for atendida
nota = float(input('Informe a nota do aluno: '))
comportado = True if input('Comportado (y/n): ') == 'y' else False

# o primeiro 'True' executa o bloco e ignora o resto
if nota >= 9 and comportado:
    print('Duas palavras: para bens! :P')
    print('Quadro de Honra')
elif nota >= 7:
    print('Aprovado')
elif nota >= 5.5:
    print('Recuperacao')
elif nota >= 3.5:
    print('Recuperacao + Trabalho')
else:
    print('Reprovado')

print(nota)