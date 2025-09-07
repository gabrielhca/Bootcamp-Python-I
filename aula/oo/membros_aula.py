class Contador:
    # atributo de class, pertence a classe e é compartilhado por todas as instancias
    contador = 10 

    # metodo de instancia opera sobre uma instancia especifica
    def inst_maluco(self):
        self.contador = self.contador + 1
        return self.contador

    # @classmethod mEtodo de classe opera sobre a classe
    @classmethod
    def inc(cls):
        # altera o atributo da classe
        cls.contador += 1
        return cls.contador

    @classmethod
    def dec(cls):
        cls.contador -= 1
        return cls.contador
    
    # metodo estatico
    def mais_um(n):
        return n + 1
    
c1 = Contador()
# chama o metodo da instancia
print(c1.inst_maluco())
print(c1.inst_maluco())
print(c1.inst_maluco())
# chama o metodo de classe
print(Contador.inc())
print(Contador.inc())
print(Contador.inc())
print(Contador.inc())
print(Contador.dec())
print(Contador.dec())
print(Contador.dec())
# chama o metodo estatico
print(Contador.mais_um(99))
