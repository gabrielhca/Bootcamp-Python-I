# uma classe é um modelo para criar objetos
class Produto:
    # __init__ é o construtor
    # 'self' se refere ao proprio
    def __init__(self, nome, preco = 1.99, desc=0):
        self.nome = nome
        # Usar '__' torna o atributo privado
        self.__preco = preco
        self.desc = desc
    
    # @property permite acessar um metodo como se fosse um atributo
    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, novo_preco):
        if novo_preco > 0:
            self.__preco = novo_preco

    # metodo é uma função que pertence a classe
    @property
    def preco_final(self):
        return (1 - self.desc) *  self.preco

# p1 e p2 são instancias/objetos da classe Produto.
p1 = Produto('Caneta', 10, 0.1) # Produto.__init__(p1)
p2 = Produto('Caderno', 14, 0.5)

p1.preco = -70.00 # não altera pois é menor que zero
p2.preco = 8.99

print(p1.nome, p1.preco, p1.desc, p1.preco_final)
print(p2.nome, p2.preco, p2.desc, p2.preco_final)