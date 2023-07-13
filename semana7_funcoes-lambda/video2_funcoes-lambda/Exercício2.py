#Combine o nome e o sobrenome de uma pessoa

comp = lambda x,y: x.strip().title() + ' ' + y.strip().title()

nome = input('Informe seu nome: ')
sobrenome = input('Informe seu sobrenome: ')

print('Nome completo: ' + comp(nome, sobrenome))