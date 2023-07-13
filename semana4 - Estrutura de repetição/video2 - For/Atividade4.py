#Escreva um programa que pergunte ao usuário quantos alunos ele tem em sua sala.
#Em seguida, através de um laço FOR, peça ao usuário dar as notas de cada aluno na sala, um por vez.
#Por fim, o programa deve mostrar a média aritmética da turma.

qtdAlunos = int(input('Informe quantos alunos tem na sala: '))
soma = 0
print('')
for aluno in range(qtdAlunos):
    nota = float(input('Informe a nota do aluno ' + str(aluno+1) + ': '))
    soma += nota
else:
    media = soma / qtdAlunos
    print('')
    print('A média da sala é ' + str(media))
