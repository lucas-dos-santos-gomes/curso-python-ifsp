#Exercício 5
#Solicitar nome e peso de duas pessoas
#Apresentar o nome da pessoa mais pesada

pessoa1 = input('Informe o nome da primeira pessoa: ')
peso1 = float(input('Informe o peso da primeira pessoa: '))
print('')
pessoa2 = input('Informe o nome da segunda pessoa: ')
peso2 = float(input('Informe o peso da segunda pessoa: '))
print('')
if peso1 > peso2:
    print(pessoa1 + ' pesa ' + str(peso1) + ' quilos e é a pessoa mais pesada.')
else:
    print(pessoa2 + ' pesa ' + str(peso2) + ' quilos e é a pessoa mais pesada.')
