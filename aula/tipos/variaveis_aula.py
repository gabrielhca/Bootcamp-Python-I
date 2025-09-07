# variaveis armazenam diferentes tipos de dados
a = 3
b = 4.4

print(a + b)

texto = "Sua idade é..."
idade = 27

# f-string (f'') permite formatar strings
print(f'{texto} {idade}')

# multiplicar uma string repete o texto
saudacao = 'bom dia '
print(3 * saudacao)

PI = 3.14
# o input() sempre retorna uma string, usamos floar() para converter
raio = float(input('informe o raio da circ? '))
area = PI * pow(raio, 2)

print(f'A area da circunferencia é {area} m2.')