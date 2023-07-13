#Exercício 3
#Solicitar o tipo sanguíneo
#Caso seja do tipo A ou O
#A pessoa é um possível doador

sangue = input('Informe seu tipo sanguíneo (O/A/B/AB): ')

if sangue.upper() == 'A' or sangue.upper() == 'O':
    print('Você é um possível doador!')
print('Tipo sanguíneo informado: ' + sangue.upper())
