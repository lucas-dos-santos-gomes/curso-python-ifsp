#Exercício Bônus 1 (eu mesmo criei)
#Solicite o tamanho dos 3 lados do triângulo
#Verifique se é um triângulo equilátero, isóceles ou escaleno

lado1 = int(input('Informe o tamanho do lado UM do triângulo: '))
lado2 = int(input('Informe o tamanho do lado DOIS do triângulo: '))
lado3 = int(input('Informe o tamanho do lado TRÊS do triângulo: '))

equilatero = (lado1 == lado2 and lado2 == lado3)
isoceles = (
    (lado1 == lado2 and lado2 != lado3)
    or
    (lado1 == lado3 and lado3 != lado2)
    or
    (lado2 == lado3 and lado3 != lado1)
)
escaleno = (lado1 != lado2) and (lado2 != lado3) and (lado3 != lado1)

print('')
if equilatero == True:
    print('Todos os lados desse triângulo são iguais, portanto, ele é equilátero!')
if isoceles == True:
    print('Esse triângulo tem dois lados iguais e um lado diferente, portanto, ele é isóceles!')
if escaleno == True:
    print('Esse triângulo tem todos os lados diferentes, portanto, ele é escaleno!')

'ou'

if equilatero == True:
    "print('Todos os lados desse triângulo são iguais, portanto, ele é equilátero!')"
elif isoceles == True:
    "print('Esse triângulo tem dois lados iguais e um lado diferente, portanto, ele é isóceles!')"
else:
    "print('Esse triângulo tem todos os lados diferentes, portanto, ele é escaleno!')"

