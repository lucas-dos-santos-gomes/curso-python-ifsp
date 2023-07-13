#Faça uma aplicação que tenha uma estrutura de repetição que fique solicitando uma palavra ao usuário,
#até que o usuário informe que o programa deve encerrar.
#Após a finalização da aplicação, apresente o número de palavras que ele inseriu no sistema.

qtdPalavras = 0
continuar = input('Deseja informar uma palavra? (S/N): ')

while continuar.upper() != 'S' and continuar.upper() != 'N':
    continuar = input("Opção inválida. Informe 'S' ou 'N': ")

print('')

while continuar.upper() == 'S':
    qtdPalavras+=1
    palavra = input('Informe uma palavra: ')
    continuar = input('Deseja continuar? (S/N): ')
    while continuar.upper() != 'S' and continuar.upper() != 'N':
        continuar = input("Opção inválida. Informe 'S' ou 'N': ")
    print('')

if qtdPalavras == 1:
    print('Você informou ' + str(qtdPalavras) + ' palavra no sistema.')
else:
    print('Você informou ' + str(qtdPalavras) + ' palavras no sistema.')
