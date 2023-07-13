#Desenvolva uma aplicação que faça o cadastro de pessoas para um sistema de Recursos Humanos.
#O cadastrado deverá responder se sabe utilizar o computador e o seu nível idioma inglês.
#Ao final, deverá apresentar:
# => quantidade de pessoas que sabem utilizar um computador;
# => quantidade de pessoas com nível básico de inglês;
# => quantidade de pessoas com nível intermediário de inglês;
# => quantidade de pessoas com nível avançado de inglês;
# => quantidade de pessoas com nível avançado de inglês que sabem utilizar um computador.

print('')
print('******************** Recursos Humanos ********************')

numCadastro = 0
pc = 0
basico = 0
inter = 0
avan = 0
pcAvan = 0

cadastro = input('Deseja efetuar um cadastro? (S/N): ')

while cadastro.upper() != 'S' and cadastro.upper() != 'N':
    cadastro = input("Resposta incorreta. Digite 'S' ou 'N': ")

print('')

while cadastro.upper() == 'S':
    nome = input('Informe o nome do candidato ' + str(numCadastro + 1) + ': ')
    print('')

    computador = input('Sabe utilizar um computador? (S/N): ')
    while computador.upper() != 'S' and computador.upper() != 'N':
        computador = input("Resposta incorreta. Digite 'S' ou 'N': ")
    print('')

    ingles = input('Qual o nível de inglês? ')
    while(
        ingles.title() != 'Básico'
        and
        ingles.title() != 'Basico'
        and
        ingles.title() != 'Intermediário'
        and
        ingles.title() != 'Intermediario'
        and
        ingles.title() != 'Avançado'
        and
        ingles.title() != 'Avancado'
    ):
        ingles = input("Dados incorretos. Informe o nivel 'Básico', 'Intermediário' ou 'Avançado': ")
    print('')

    if computador.upper() == 'S':
        pc += 1

    if ingles.title() == 'Básico' or ingles.title() == 'Basico':
        basico += 1
    elif ingles.title() == 'Intermediário' or ingles.title() == 'Intermediario':
        inter += 1
    elif ingles.title() == 'Avançado' or ingles.title() == 'Avancado':
        avan += 1

    if ingles.title() == 'Avançado' or ingles.title() == 'Avancado' and computador.upper() == 'S':
        pcAvan += 1

    cadastro = input('Deseja fazer outro cadastro? (S/N): ')
    while cadastro.upper() != 'S' and cadastro.upper() != 'N':
        cadastro = input("Resposta incorreta. Digite 'S' ou 'N': ")
    print('')

    if cadastro.upper() == 'S':
        print('')
        print('********** Próximo candidato **********')
        print('')

    numCadastro += 1
else:
    print('')
    print('********** Resultado final **********')
    print('')
    print('')

print('Quantidade de cadastrados = ' + str(numCadastro))
print('')
print('Quantidade de cadastrados que sabem utilizar um computador = ' + str(pc))
print('')
print('Quantidade de cadastrados que tem nível básico de inglês = ' + str(basico))
print('Quantidade de cadastrados que tem nível intermediário de inglês = ' + str(inter))
print('Quantidade de cadastrados que tem nível avançado de inglês = ' + str(avan))
print('')
print('Quantidade de cadastrados que sabem utilizar um computador e tem nível avançado de inglês = ' + str(pcAvan))
print('')
print('')
print('Fim da aplicação')
