#Use as funções recursivas para calcular a escala de Fibonacci.
#Essa escala aumenta com a soma dos dois números antecessores ( 1 1 2 3 5 8 13...)

def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)
posicao = int(input('Informe a posição do Fibonacci: '))
resultado = fibonacci(posicao)
print('Fibonacci (' + str(posicao) + 'º posição) = %d' %resultado)
