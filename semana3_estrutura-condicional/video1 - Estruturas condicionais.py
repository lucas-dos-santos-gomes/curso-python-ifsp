#Exercício 1
#Informe um valor
#Verifique se esse valor é maior que 100
#Caso seja verdadeiro, calcule 10% desse valor

valor = int(input('Informe um valor: '))
if valor > 100:
    valor = valor * 0.1
print('O valor é: ' + str(valor))

print('')
print('******************************************************************************************************')
print('')

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

print('')
print('******************************************************************************************************')
print('')

#Exercício 3
#Solicitar o tipo sanguíneo
#Caso seja do tipo A ou O
#A pessoa é um possível doador

sangue = input('Informe seu tipo sanguíneo (O/A/B/AB): ')

if sangue.upper() == 'A' or sangue.upper() == 'O':
    print('Você é um possível doador!')
print('Tipo sanguíneo informado: ' + sangue.upper())

print('')
print('******************************************************************************************************')
print('')

#Exercício 4
#Solicitar ao usário 3 notas
#Calcular a média
#Caso média seja menor que 6, msg para aumentar a dedicação
#Caso média seja maior ou igual a 6, msg de continue assim

aluno = input('Insira seu nome completo: ')
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

print('')
print('******************************************************************************************************')
print('')

#Exercício 5
#Solicitar nome e peso de duas pessoas
#Apresentar o nome da pessoa mais pesada

pessoa1 = input('Informe o nome da primeira pessoa: ')
peso1 = float(input('Informe o peso da primeira pessoa: '))
print('')
pessoa2 = input('Informe o nome da segunda pessoa: ')
peso2 = float(input('Informe o peso da segunda pessoa: '))
print('')
if peso1 > peso2:
    print(pessoa1 + ' pesa ' + str(peso1) + ' quilos e é a pessoa mais pesada.')
else:
    print(pessoa2 + ' pesa ' + str(peso2) + ' quilos e é a pessoa mais pesada.')

print('')
print('******************************************************************************************************')
print('')

#Exercício 6
#Solicite 3 valores e verifique se forma um triângulo equilátero

lado1 = int(input('Informe o tamanho do lado 1: '))
lado2 = int(input('Informe o tamanho do lado 2: '))
lado3 = int(input('Informe o tamanho do lado 3: '))
print('')
if lado1 == lado2 and lado2 == lado3:
    print('Esse triângulo é equilátero!')
else:
    print('Esse triângulo não é equilátero.')

print('')
print('******************************************************************************************************')
print('')

#Exercício 7
#Solicite 2 valores
#Faça a potenciação do primeiro valor pelo segundo
#Verifique se essa potência é um valor 'par' ou 'ímpar'

valor1 = int(input('Informe valor 1: '))
valor2 = int(input('Informe valor 2: '))
potencia = valor1 ** valor2
print('')
print('A potência dos valores é ' + str(potencia))
if (potencia % 2) == 0:
    print('O valor da potência é PAR')
else:
    print('O valor da potência é ÍMPAR')

print('')
print('******************************************************************************************************')
print('')

#Exercício Bônus 1 (eu mesmo criei)
#Solicite o tamanho dos 3 lados do triângulo
#Verifique se é um triângulo equilátero, isóceles ou escaleno

lado1 = int(input('Informe o tamanho do lado UM do triângulo: '))
lado2 = int(input('Informe o tamanho do lado DOIS do triângulo: '))
lado3 = int(input('Informe o tamanho do lado TRÊS do triângulo: '))

equilatero = (lado1 == lado2 and lado2 == lado3)
isoceles = (
    (lado1 == lado2 and lado2 != lado3)
    or
    (lado1 == lado3 and lado3 != lado2)
    or
    (lado2 == lado3 and lado3 != lado1)
)
escaleno = (lado1 != lado2) and (lado2 != lado3) and (lado3 != lado1)

print('')
if equilatero == True:
    print('Todos os lados desse triângulo são iguais, portanto, ele é equilátero!')
if isoceles == True:
    print('Esse triângulo tem dois lados iguais e um lado diferente, portanto, ele é isóceles!')
if escaleno == True:
    print('Esse triângulo tem todos os lados diferentes, portanto, ele é escaleno!')

'ou'

if equilatero == True:
    "print('Todos os lados desse triângulo são iguais, portanto, ele é equilátero!')"
elif isoceles == True:
    "print('Esse triângulo tem dois lados iguais e um lado diferente, portanto, ele é isóceles!')"
else:
    "print('Esse triângulo tem todos os lados diferentes, portanto, ele é escaleno!')"

print('')
print('******************************************************************************************************')
print('')

#Exercício Bônus 2 (eu mesmo criei)
#Peça para o usuário informar as peças do uniforme de jogo que ele está usando
#Verifique se as peças formam o uniforme completo
#O uniforme precisa de alguma camisa, short, chuteira, meiao, caneleira e não pode ter nenhum acessório

print('')
print('Vamos avaliar se o seu uniforme está correto ou não e, assim, decidir sua entrada no jogo.')
nome = input('Informe seu nome: ')
nome = nome.title()

print('')

print('Informe qual camisa do uniforme você está usando.')
camisaMangaCurta = input('Camisa de manga curta (S/N): ')
if camisaMangaCurta.upper() == 'S':
    camisaMangaCurta = True
elif camisaMangaCurta.upper() == 'N':
    camisaMangaCurta = False

camisaMangaLonga = input('Camisa de manga longa (S/N): ')
if camisaMangaLonga.upper() == 'S':
    camisaMangaLonga = True
elif camisaMangaLonga.upper() == 'N':
    camisaMangaLonga = False

camisaRegata = input('Camisa regata (S/N): ')
if camisaRegata.upper() == 'S':
    camisaRegata = True
elif camisaRegata.upper() == 'N':
    camisaRegata = False

print('')

print('Agora, informe qual calção do uniforme você está usando.')
calcaoPreto = input('Calção preto (S/N): ')
if calcaoPreto.upper() == 'S':
    calcaoPreto = True
elif calcaoPreto.upper() == 'N':
    calcaoPreto = False

calcaoBranco = input('Calção branco (S/N): ')
if calcaoBranco.upper() == 'S':
    calcaoBranco = True
elif calcaoBranco.upper() == 'N':
    calcaoBranco = False

print('')

print('Agora, informe se você está usando as peças para o pé e as pernas.')
chuteira = input('Chuteira (S/N): ')
if chuteira.upper() == 'S':
    chuteira = True
elif chuteira.upper() == 'N':
    chuteira = False

meiao = input('Meião (S/N): ')
if meiao.upper() == 'S':
    meiao = True
elif meiao.upper() == 'N':
    meiao = False

caneleira = input('Caneleira (S/N): ')
if caneleira.upper() == 'S':
    caneleira = True
elif caneleira.upper() == 'N':
    caneleira = False

print('')

print('Por último, informe se você está usando algum tipo de acessório extra')
brinco = input('Brinco (S/N): ')
if brinco.upper() == 'S':
    brinco = True
elif brinco.upper() == 'N':
    brinco = False

piercing = input('Piercing (S/N): ')
if piercing.upper() == 'S':
    piercing = True
elif piercing.upper() == 'N':
    piercing = False

relogio = input('Relógio (S/N): ')
if relogio.upper() == 'S':
    relogio = True
elif relogio.upper() == 'N':
    relogio = False

pulseira = input('Pulseira (S/N): ')
if pulseira.upper() == 'S':
    pulseira = True
elif pulseira.upper() == 'N':
    pulseira = False

colar = input('Colar (S/N): ')
if colar.upper() == 'S':
    colar = True
elif colar.upper() == 'N':
    colar = False

corrente = input('Corrente (S/N): ')
if corrente.upper() == 'S':
    corrente = True
elif corrente.upper() == 'N':
    corrente = False

uniforme = (
    (camisaMangaCurta or camisaMangaLonga or camisaRegata)
    and
    (calcaoPreto or calcaoBranco)
    and
    (chuteira and meiao and caneleira)
)
acessorio = (brinco + piercing + relogio + pulseira + colar + corrente)

print('')

if (uniforme == True) and (acessorio == 0):
    print(nome + ', você está usando o uniforme completo.')
    print('Pode ir jogar!')
elif (uniforme == True) and (acessorio != 0):
    print(nome + ', você está usando o uniforme completo, porém, acessórios não são permitidos.')
    print('Volte outro dia!')
else:
    print(nome + ', o seu uniforme esá incompleto.')
    print('Volte outro dia!')
