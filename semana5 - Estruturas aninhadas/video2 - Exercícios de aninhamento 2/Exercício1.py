#Desenvolva uma aplicação que repita a inserção de dados de alunos (nome, nota1, nota2 e nota3)
#até que o usuário peça para parar a aplicação.
#As notas para serem consideradas válidas devem estar entre 0 e 10. Apresente ao final:
# => Quantidade de alunos aprovados (média >= 7);
# => Quantidade de alunos reprovados (média < 4);
# => Quantidade de alunos de exame final (média >= 4 e média < 7).

contador = 0
aprovados = 0
reprovados = 0
exameFinal = 0

dados = input('Deseja inserir dados de um aluno? (S/N): ')
while dados.upper() != 'S' and dados.upper() != 'N':
    dados = input("Resposta inválida. Digite 'S' para Sim e 'N' para Não: ")
print('')

while dados.upper() == 'S':
    nome = input('Insira o nome do aluno ' + str(contador + 1) + ': ')
    for nota in range(1,4):
        if nota == 1:
            nota1 = float(input('Insira a nota de caderno de ' + nome.title() + ': '))
            while nota1 < 0 or nota1 > 10:
                print('Nota inválida. O valor da nota precisa estar entre 0 e 10')
                nota1 = float(input('Insira a nota de caderno de ' + nome.title() + ': '))
        elif nota == 2:
            nota2 = float(input('Insira a nota de participação de ' + nome.title() + ': '))
            while nota2 < 0 or nota2 > 10:
                print('Nota inválida. O valor da nota precisa estar entre 0 e 10')
                nota2 = float(input('Insira a nota de participação de ' + nome.title() + ': '))
        else:
            nota3 = float(input('Insira a nota da prova de ' + nome.title() + ': '))
            while nota3 < 0 or nota3 > 10:
                print('Nota inválida. O valor da nota precisa estar entre 0 e 10')
                nota3 = float(input('Insira a nota da prova de ' + nome.title() + ': '))
    media = (nota1 + nota2 + nota3) / 3
    if media >= 7:
        aprovados += 1
    elif media < 4:
        reprovados += 1
    else:
        exameFinal += 1

    print('')
    print('A média de ' + nome.title() + ' é %.1f' %media)
    print('')

    dados = input('Deseja inserir os dados de outro aluno? (S/N): ')
    while dados.upper() != 'S' and dados.upper() != 'N':
        dados = input("Resposta inválida. Digite 'S' para Sim e 'N' para Não: ")
    print('')

    if dados.upper() == 'S':
        print('')
        print('******************** Próximos dados ********************')
        print('')

    contador += 1
else:
    print('')
    print('******************** Resutado final ********************')
    print('')

print('Quantidade de alunos: ' + str(contador))
print('Quantidade de alunos aprovados (média maior ou igual à 7): ' + str(aprovados))
print('Quantidade de alunos reprovados (média menor que 4): ' + str(reprovados))
print('Quantidade de alunos de exame final (média entre 4 e 7): ' + str(exameFinal))
print('')
print('Fim da aplicação')
