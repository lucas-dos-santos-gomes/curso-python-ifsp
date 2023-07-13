#Exercício 1
#Desenvolva uma aplicação que solicite ao usuário seu nome
#Verifique se o nome do usuário começa com 'Lucas'

nomeUsuário = input('Informe o seu nome: ')
print(nomeUsuário[0:5].title() == 'Lucas')

print('')
print('******************************************************************************************************')
print('')

#Exercício 2
#Solicite ao usuário que informe o seu nome
#Verifique se existe a palavra 'Gomes' em qualquer parte do nome

nome = input('Informe o seu nome: ')
nome = nome.title()
print(nome.find('Gomes') >= 0)
#ou
print('Gomes' in nome)

print('')
print('******************************************************************************************************')
print('')

#Exercício 3
#Solicite ao usuário que informe uma frase
#Mostre a frase em maiúsculo
#Mostre a frase em minúsculo
#Mostre a quantidade de caracteres sem contar os espaços

frase = input('Escreva uma frase: ')
print('')
print('Frase em maiúsculo: ' + frase.upper())
print('Frase em minúsculo: ' + frase.lower())
print('')
print('Essa frase possui ' + str(len(frase) - frase.count(' ')) + ' caracteres.')

