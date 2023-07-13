#Crie uma lista de 20 posições com números aleatórios variando entre 1000 e 2000

import random as rd

lista = []
for i in range(20):
    x = rd.randrange(1000, 2000)
    lista.append(x)
print(lista)