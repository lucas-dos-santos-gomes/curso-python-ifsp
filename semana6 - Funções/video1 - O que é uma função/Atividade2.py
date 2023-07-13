#Use as funções para fazer o cálculo fatorial de um número utilizando a recursividade.
#Recursividade = ter a função chamando a ela própria

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n-1)

numero = int(input('Informe o número: '))
print(str(numero) + '! = ' + str(fatorial(numero)))
