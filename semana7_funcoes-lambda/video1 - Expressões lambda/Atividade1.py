#Construa uma aplicação utilizando função e expressão lambda para comparação de sintaxe.

#função normal
def ad(n1, n2):
    return n1 + n2

#função lambda
sub = lambda a,b: a-b

num1 = int(input('Informe o número 1: '))
num2 = int(input('Informe o número 2: '))

print('')

print('Função normal (' + str(num1) + ' + ' + str(num2) + ') = ' + str(ad(num1,num2)))
print('Função lambda (' + str(num1) + ' - ' + str(num2) + ') = ' + str(sub(num1,num2)))