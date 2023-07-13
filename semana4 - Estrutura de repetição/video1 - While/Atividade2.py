#Faça uma aplicação que receba o nome e o sexo de uma pessoa
#Sendo no sexo o valor M para Masculino e F para Feminino
#Ao final apresente o nome e o sexo da pessoa

nome = input('Informe seu nome: ')
sexo = input('Informe seu sexo (M/F): ')
print('')
while sexo.upper() != 'M' and sexo.upper() != 'F':
    sexo = input('Sexo incorreto. Informe M ou F: ')
print('')
if sexo.upper() == 'M':
    print(nome.title() + ' é do sexo masculino.')
elif sexo.upper() == 'F':
    print(nome.title() + ' é do sexo feminino.')
