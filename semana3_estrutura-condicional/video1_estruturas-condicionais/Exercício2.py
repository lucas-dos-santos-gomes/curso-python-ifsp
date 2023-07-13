#Exercício 2
#Solicite ao usuário seu sexo e a sua idade
#Caso idade seja maior ou igual a 18
# e o sexo seja masculino
#Vamos solicitar a carteira de reservista

sexo = input('Informe o sexo (M/F): ')
idade = int(input('Informe sua idade: '))

if sexo.upper() == 'M' and idade >= 18:
    print('Serviço militar obrigatório!')
    cartReservista = input('Informe sua carteira de reservista: ')
    print('Todos os dados foram coletados.')
print('')
print('Fim da aplicação.')