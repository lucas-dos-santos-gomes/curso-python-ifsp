#Crie uma lista com números aleatórios limitados a 100

import random
lista = []
for i in range(10):
    x = random.randrange(100)
    lista.append(x)
print(lista)