#Escreva um programa que solicita 10 números ao usuário com while e, ao final, mostre:
#qual desses números é o maior.
#qual desses números é o menor.
#qual é a média dos números.

quantidade = 1
soma = 0

while quantidade < 11:
    numero = int(input('Informe um número (' + str(quantidade) + '): '))
    if quantidade == 1:
        maior = numero
        menor = numero
    elif numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero

    soma += numero
    quantidade += 1
else:
    media = soma / quantidade
    print('')

print('O maior valor é: ' + str(maior))
print('O menor valor é: ' + str(menor))
print('A média dos valores é: ' + str(media))
