class Contador:
    contador = 10 # atributo de class

    def inst_maluco(self):
        self.contador = self.contador + 1
        return self.contador

    @classmethod
    def inc(cls):
        cls.contador += 1
        return cls.contador

    @classmethod
    def dec(cls):
        cls.contador -= 1
        return cls.contador
    
    def mais_um(n):
        return n + 1
    
c1 = Contador()
print(c1.inst_maluco())
print(c1.inst_maluco())
print(c1.inst_maluco())

print(Contador.inc())
print(Contador.inc())
print(Contador.inc())
print(Contador.inc())
print(Contador.dec())
print(Contador.dec())
print(Contador.dec())
print(Contador.mais_um(99))
