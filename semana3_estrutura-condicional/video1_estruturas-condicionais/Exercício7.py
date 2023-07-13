#Exercício 7
#Solicite 2 valores
#Faça a potenciação do primeiro valor pelo segundo
#Verifique se essa potência é um valor 'par' ou 'ímpar'

valor1 = int(input('Informe valor 1: '))
valor2 = int(input('Informe valor 2: '))
potencia = valor1 ** valor2
print('')
print('A potência dos valores é ' + str(potencia))
if (potencia % 2) == 0:
    print('O valor da potência é PAR')
else:
    print('O valor da potência é ÍMPAR')
