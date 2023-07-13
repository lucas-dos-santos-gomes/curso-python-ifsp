#Faça uma lista que retorne outra lista de números pares maiores que 10

lista = []
i = int(input('Informe um número para a lista: '))
lista.append(i)
print('Lista = ' + str(lista))

continuar = input('Deseja adicionar mais um número na lista? (S/N): ').upper()
while continuar != 'S' and continuar != 'N':
    continuar = input('Resposta incorreta. Digite \'S\' (SIM) ou \'N\' (NÃO): ').upper()

print()

while continuar == 'S':
    i = int(input('Informe outro número para a lista: '))
    lista.append(i)
    print('Lista = ' + str(lista))

    continuar = input('Deseja adicionar mais um número na lista? (S/N): ').upper()
    while continuar != 'S' and continuar != 'N':
        continuar = input('Resposta incorreta. Digite \'S\' (SIM) ou \'N\' (NÃO): ').upper()
    print()
else:
    par10 = list(filter(lambda x: (x % 2 == 0) and (x > 10), lista))
    print('Lista normal = ' + str(lista))
    print('Lista de pares maiores que 10 = ' + str(par10))