#Exercício 1
#Informe um valor
#Verifique se esse valor é maior que 100
#Caso seja verdadeiro, calcule 10% desse valor

valor = int(input('Informe um valor: '))
if valor > 100:
    valor = valor * 0.1
print('O valor é: ' + str(valor))
