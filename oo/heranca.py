# classe pai
class Carro:
    def __init__(self):
        self.__velocidade = 0

    @property
    def velocidade(self):
        return self.__velocidade

    def acelerar(self):
        self.__velocidade += 5
        return self.__velocidade
    
    def frear(self):
        self.__velocidade -= 5
        return self.__velocidade
    
# Uno herda tudo de Carro
class Uno(Carro):
    pass
# Ferrari herda tudo de Carro
class Ferrari(Carro):
    def acelerar(self):
        # 'super().acelerar()' chama o metodo 'acelerar' da classe pai
        super().acelerar()
        return super().acelerar()

c1 = Ferrari()
print(c1.acelerar())
print(c1.acelerar())
print(c1.acelerar())
print(c1.frear())
print(c1.frear())
print(c1.frear())