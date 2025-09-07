# funções são blocos de codigo reutilizaveis definidos pela chave 'def'
def saudacao(nome = 'Pessoa', idade = 20):
    print(f'Bom dia {nome}!\nVc nem parece ter {idade} anos!')

#def saudacao():
#    print('Boa tarde!')

# 'return' retorna valores de uma função
def soma_e_multi(a, b, x):
    return a + b * x

# garante que esse bloco so é executado dentro do arquivo principal
if __name__ == '__main__':
    saudacao('Ana', idade=30)