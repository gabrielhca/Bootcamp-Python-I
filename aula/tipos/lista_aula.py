# listas são coleções ordenadas, mutaveis e que aceitam valores duplicados
nums = [1, 2, 3]
print(type(nums))

# apeend() adiciona um valor ao final da lista
nums.append(3)
nums.append(3)
nums.append(500)
# len() retorna o tamanho da lista
print(len(nums))

# listas são mutaveis, então podemos alterar um elmento pelo indice
nums[3] = 100
# insert() adiciona um elemento em um indice especifico
nums.insert(0, -200)

# indice negativo conta a parti do final da lista
# -1 é o ultimo elemento, -2 o penultimo e assim por diante
print(nums[-1])

print(nums)