#faça uma função que calcule a área de um círculo

import math

def area(r):
    areaCirculo = math.pi * r**2
    print('A área desse círculo é %.2f' %areaCirculo)

raio = int(input('Defina o raio do círculo: '))
area(raio)
