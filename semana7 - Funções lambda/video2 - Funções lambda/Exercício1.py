#Programe uma filtragem apenas dos itens pares de uma lista

lista = []
num = int(input('Insira um número para a lista: '))
lista.append(num)
print('Lista = ' + str(lista))

continuar = input('Deseja inserir mais um número na lista? (S/N): ').upper()
while continuar != 'S' and continuar != 'N':
    continuar = input('Resposta incorreta. Digite \'S\' (SIM) ou \'N\' (NÃO): ').upper()

print()

while continuar == 'S':
    num = int(input('Insira um número para a lista: '))
    lista.append(num)
    print('Lista = ' + str(lista))

    continuar = input('Deseja inserir mais um número na lista? (S/N): ').upper()
    while continuar != 'S' and continuar != 'N':
        continuar = input('Resposta incorreta. Digite \'S\' (SIM) ou \'N\' (NÃO): ').upper()
    print()
else:
    pares = list(filter(lambda x: x%2 == 0, lista))
print('Lista normal = ' + str(lista))
print('Lista de pares = ' + str(pares))