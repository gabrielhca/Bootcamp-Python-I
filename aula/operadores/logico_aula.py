# operadores logicos combinam expressões booleanas
b1 = True
b2 = False
b3 = True

print(b1 and b2 and b3)
print(b1 or b2 or b3)
print(b1 != b2) # xor
print(not b1)
print(not b2)

# combinação de operadores
print(b1 and not b2 and b3)

x = 3
y = 4

# operadores logicos avaliam da esquerda para direita
print(b1 and not b2 and x < y)