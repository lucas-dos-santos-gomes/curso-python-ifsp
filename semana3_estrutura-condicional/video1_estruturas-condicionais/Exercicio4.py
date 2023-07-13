#Exercício 4
#Solicitar ao usário 3 notas
#Calcular a média
#Caso média seja menor que 6, msg para aumentar a dedicação
#Caso média seja maior ou igual a 6, msg de continue assim

aluno = input('Insira seu nome: ')
print('')
nota1 = float(input('Insira a nota da prova: '))
nota2 = float(input('Insira a nota do caderno: '))
nota3 = float(input('Insira a nota de participação em aula: '))
print('')
media = (nota1 + nota2 + nota3) / 3
if media < 6:
    print(aluno.title() + ', a sua média é ' + str(media) + ' e esta abaixo do requerido. Aumente a dedicação aos estudos!')
else:
    print(aluno.title() + ', a sua média é ' + str(media) + '. Continue assim!')
