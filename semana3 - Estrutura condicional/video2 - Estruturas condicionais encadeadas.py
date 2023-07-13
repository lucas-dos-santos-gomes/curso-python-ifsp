#Ler o nome de três pessoas e seus pesos
#Mostre os dados (nome e peso) em ordem decrescente de peso

nome1 = input('Informe o nome da pessoa 1: ')
peso1 = float(input('Informe o peso da pessoa 1: '))
print('')
nome2 = input('Informe o nome da pessoa 2: ')
peso2 = float(input('Informe o peso da pessoa 2: '))
print('')
nome3 = input('Informe o nome da pessoa 3: ')
peso3 = float(input('Informe o peso da pessoa 3: '))

nome1 = nome1.title()
nome2 = nome2.title()
nome3 = nome3.title()

print('')

if peso1 > peso2 and peso2 > peso3:
    print('Ordem Decrescente (+pesado -> +leve):')
    print('1- ' + nome1 + '(' + str(peso1) + 'kg)')
    print('2- ' + nome2 + '(' + str(peso2) + 'kg)')
    print('3- ' + nome3 + '(' + str(peso3) + 'kg)')
elif peso1 > peso3 and peso3 > peso2:
    print('Ordem Decrescente (+pesado -> +leve):')
    print('1- ' + nome1 + '(' + str(peso1) + 'kg)')
    print('2- ' + nome3 + '(' + str(peso3) + 'kg)')
    print('3- ' + nome2 + '(' + str(peso2) + 'kg)')
elif peso2 > peso1 and peso1 > peso3:
    print('Ordem Decrescente (+pesado -> +leve):')
    print('1- ' + nome2 + '(' + str(peso2) + 'kg)')
    print('2- ' + nome1 + '(' + str(peso1) + 'kg)')
    print('3- ' + nome3 + '(' + str(peso3) + 'kg)')
elif peso2 > peso3 and peso3 > peso1:
    print('Ordem Decrescente (+pesado -> +leve):')
    print('1- ' + nome2 + '(' + str(peso2) + 'kg)')
    print('2- ' + nome3 + '(' + str(peso3) + 'kg)')
    print('3- ' + nome1 + '(' + str(peso1) + 'kg)')
elif peso3 > peso1 and peso1 > peso2:
    print('Ordem Decrescente (+pesado -> +leve):')
    print('1- ' + nome3 + '(' + str(peso3) + 'kg)')
    print('2- ' + nome1 + '(' + str(peso1) + 'kg)')
    print('3- ' + nome2 + '(' + str(peso2) + 'kg)')
elif peso3 > peso2 and peso2 > peso1:
    print('Ordem Decrescente (+pesado -> +leve):')
    print('1- ' + nome3 + '(' + str(peso3) + 'kg)')
    print('2- ' + nome2 + '(' + str(peso2) + 'kg)')
    print('3- ' + nome1 + '(' + str(peso1) + 'kg)')
else:
    print('Indefinido')

#outra forma de ser feito:
print('')

if peso1 > peso2 and peso1 > peso3:
    print('O nome do mais pesado é ' + nome1 + ' e seu peso é ' + str(peso1))
    if peso2 > peso3:
        print('O nome com peso médio é ' + nome2 + ' e o seu peso é ' + str(peso2))
        print('O nome do mais leve é ' + nome3 + ' e seu peso é ' + str(peso3))
    else:
        print('O nome com peso médio é ' + nome3 + ' e o seu peso é ' + str(peso3))
        print('O nome do mais leve é ' + nome2 + ' e seu peso é ' + str(peso2))

elif peso2 > peso1 and peso2 > peso3:
    print('O nome do mais pesado é ' + nome2 + ' e seu peso é ' + str(peso2))
    if peso1 > peso3:
        print('O nome com peso médio é ' + nome1 + ' e o seu peso é ' + str(peso1))
        print('O nome do mais leve é ' + nome3 + ' e seu peso é ' + str(peso3))
    else:
        print('O nome com peso médio é ' + nome3 + ' e o seu peso é ' + str(peso3))
        print('O nome do mais leve é ' + nome1 + ' e seu peso é ' + str(peso1))

else:
    print('O nome do mais pesado é ' + nome3 + ' e seu peso é ' + str(peso3))
    if peso1 > peso2:
        print('O nome com peso médio é ' + nome1 + ' e o seu peso é ' + str(peso1))
        print('O nome do mais leve é ' + nome2 + ' e seu peso é ' + str(peso2))
    else:
        print('O nome com peso médio é ' + nome2 + ' e o seu peso é ' + str(peso2))
        print('O nome do mais leve é ' + nome1 + ' e seu peso é ' + str(peso1))
print('')
print('Fim da aplicação')
