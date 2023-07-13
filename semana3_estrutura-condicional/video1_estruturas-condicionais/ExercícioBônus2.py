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
#   and
#   not(brinco or piercing or relogio or pulseira or colar or corrente)
)
acessorio = (brinco + piercing + relogio + pulseira + colar + corrente)
#acessorio = (brinco or piercing or relogio or pulseira or colar or corrente)

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
