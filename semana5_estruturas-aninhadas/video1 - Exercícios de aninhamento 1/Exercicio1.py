#Desenvolva uma aplicação para o cadastro de doadores de sangue.
#Nesta etapa, solicicte o número total de pessoas que serão cadastradas.
#Para a pessoa estar apta a doação de sangue, ela não pode ter tido resfriado nos últimos 7 dias.
#Ao final, devemos apresentar a quantidade total de pessoas aptas a doação de sangue.
#Apresentar a quantidade de pessoas do sexo masculino e feminino para a doação de sangue.

quantidade = int(input('Informe o número de cadastros: '))
totF = 0
totM = 0

for qd in range(quantidade):
    nome = input('Informe o nome da pessoa ' + str(qd+1) + ': ')
    print('')
    sexo = input('Informe o sexo da pessoa ' + str(qd+1) + ' (M/F): ')
    while sexo.upper() != 'M' and sexo.upper() != 'F':
        sexo = input("Sexo inválido. Digite 'M' ou 'F': ")
    print('')

    resfriado = input('Algum sintoma de resfriado nos últimos 7 dias? (S/N): ')
    while resfriado.upper() != 'S' and resfriado.upper() != 'N':
        resfriado = input("Resposta inválida. Digite 'S' ou 'N': ")
    print('')

    if sexo.upper() == 'F' and resfriado.upper() == 'N':
        totF += 1
    elif sexo.upper() == 'M' and resfriado.upper() == 'N':
        totM += 1

    if qd != quantidade - 1:
        print('')
        print('********** Próximo registro **********')
        print('')

else:
    print('')
    print('********** Resultado final **********')
    print('')

print('Total de mulheres aptas a doação = ' + str(totF))
print('Total de homens aptos a doação = ' + str(totM))
print('Total de doadores aptos a doação = ' + str(totF + totM))
print('')
print('Fim da aplicação')
