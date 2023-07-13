#Fazer uma função que irá retornar os resultados de operações entre dois números:
# => Retornar se o primeiro número é par;
# => Retornar a multiplicação do primeiro pelo segundo.

# Meu jeito
def funcaoMult(num1, num2):
    mult = num1 * num2
    funcaoPar(num1)
    print(str(num1) + ' x ' + str(num2) + ' = ' + str(mult))

def funcaoPar(n):
    print('')
    print('Meu jeito:')
    if n%2 == 0:
        print("O número um é '%d' e ele é par." %n)
    else:
        print("O número um é '%d' e ele não é par." %n)

# Jeito do professor
def calcular(x, y):
    print()
    print('Jeito do professor:')
    return x%2==0, x*y

#*************************************************************************

n1 = int(input('Informe número 1: '))
n2 = int(input('Informe número 2: '))

funcaoMult(n1, n2)
print(calcular(n1, n2))
