#Faça uma aplicação que receba um número e mostre os próximos três

numero = int(input('Informe um número: '))
contador = 1
print('O número informado foi ' + str(numero))
while (contador <= 3):
    numero+=1
    print('Próximo: ' + str(numero))
    contador+=1
print('Fim da aplicação')
