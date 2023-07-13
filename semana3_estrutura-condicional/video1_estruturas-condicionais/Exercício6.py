#Exercício 6
#Solicite 3 valores e verifique se forma um triângulo equilátero

lado1 = int(input('Informe o tamanho do lado 1: '))
lado2 = int(input('Informe o tamanho do lado 2: '))
lado3 = int(input('Informe o tamanho do lado 3: '))
print('')
if lado1 == lado2 and lado2 == lado3:
    print('Esse triângulo é equilátero!')
else:
    print('Esse triângulo não é equilátero.')
