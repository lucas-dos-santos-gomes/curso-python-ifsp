#Head
def l():
    print()
m = lambda x, y, z: (x+y+z) / 3
p = lambda a, b: (a * 100) / b

totalAlunos = 0
aprov = 0
exame = 0
reprov = 0
aprovF = 0
aprovM = 0
exameF = 0
exameM = 0
reprovF = 0
reprovM = 0
sexoF = 0
sexoM = 0


#Body
projeto = ' Controle de Lançamento de Notas '
print(projeto.center(70, '='))

dados = input('Deseja cadastrar um aluno(a)? (S/N): ').upper().strip()
while dados != 'S' and dados != 'N':
    dados = input("Resposta inválida. Digite 'S' (Sim) ou 'N' (Não): ").upper().strip()
l()

while dados == 'S':
    cabecalho = (' Aluno %d ' %(totalAlunos + 1))
    print(cabecalho.center(70, '='))

    nome = input('Informe o nome do aluno(a): ').title()
    if nome.isalpha() == True:
        novoNome = nome.split()

    while nome.isalpha() == False:
        if nome.find(' ') > -1:
            novoNome = nome.split()
            nome = nome.replace(' ', '')
        else:
            nome = input('Nome inválido. Digite apenas letras: ').title()
            if nome.isalpha() == True:
                novoNome = nome.split()

    sexo = input('Informe o sexo de ' + novoNome[0] + ' (M/F): ').upper().strip()
    while sexo != 'M' and sexo != 'F':
        sexo = input('Resposta inválida. Digite \'M\' (Masculino) ou \'F\' (Feminino): ').upper().strip()
    l()

    nota1 = float(input('Informe a nota do caderno de {}: '.format(novoNome[0])))
    while nota1 < 0 or nota1 > 10:
        nota1 = float(input('Resposta inválida. Insira uma nota com valor entre 0 e 10: '))

    nota2 = float(input('Informe a nota da Avaliação Mensal de {}: '.format(novoNome[0])))
    while nota2 < 0 or nota2 > 10:
        nota2 = float(input('Resposta inválida. Insira uma nota com valor entre 0 e 10: '))

    nota3 = float(input('Informe a nota da Avaliação Bimestral de {}: '.format(novoNome[0])))
    while nota3 < 0 or nota3 > 10:
        nota3 = float(input('Resposta inválida. Insira uma nota com valor entre 0 e 10: '))
    l()

    media = m(nota1, nota2, nota3)
    print('A média final de {} é {:.1f}'.format(novoNome[0], media))
    l()

    if media >= 7 and sexo == 'M':
        aprov += 1
        aprovM += 1
        sexoM +=1

    elif media >= 7 and sexo == 'F':
        aprov += 1
        aprovF += 1
        sexoF += 1

    elif media >= 4 and media < 7 and sexo == 'M':
        exame += 1
        exameM += 1
        sexoM += 1

    elif media >= 4 and media < 7 and sexo == 'F':
        exame += 1
        exameF += 1
        sexoF += 1

    elif media < 4 and sexo == 'M':
        reprov += 1
        reprovM += 1
        sexoM += 1

    elif media < 4 and sexo == 'F':
        reprov += 1
        reprovF += 1
        sexoF += 1

    dados = input('Deseja cadastrar outro aluno(a)? (S/N): ').upper().strip()
    while dados != 'S' and dados != 'N':
        dados = input("Resposta inválida. Digite 'S' (Sim) ou 'N' (Não): ").upper().strip()
    l()

    totalAlunos += 1

else:
    l()
    cabecalho = ' Resultado Final '
    print(cabecalho.center(70, '='))

print('Total de alunos cadastrados: %d' %totalAlunos)

if totalAlunos == 0:
    totalAlunos += 1

print('Porcentagem de alunos aprovados: {:.1f}%'.format(p(aprov, totalAlunos)))
print('Porcentagem de alunos de exame: {:.1f}%'.format(p(exame, totalAlunos)))
print('Porcentagem de alunos reprovados: {:.1f}%'.format(p(reprov, totalAlunos)))
l()
print('Sexo Feminino: ' + str(sexoF))
print('  Aprovadas: %d' %aprovF)
print('  Exame: {}'.format(exameF))
print('  Reprovadas: ' + str(reprovF))
l()
print('Sexo Masculino: ' + str(sexoM))
print('  Aprovados: %d' %aprovM)
print('  Exame: {}'.format(exameM))
print('  Reprovados: ' + str(reprovM))
l()
print((' Fim da Aplicação ').center(70, '='))