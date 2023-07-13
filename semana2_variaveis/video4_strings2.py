print('----------')

frase = "   Aprendendo Python   "
print(frase)
carFrase = len(frase)
print(carFrase)

print('')

frase = frase.strip()
print (frase, '-', carFrase)

print('')
print('***************************************************************************************************')
print('')

nome = 'Maria'
sobrenome = 'Silva'
nomeCompleto = nome + ' ' + sobrenome
print(nomeCompleto)

print('')

string_frase = '''Olá. Esta é uma string.
Vou utilizar " ou ' para o armazenamento de strings.'''
print(string_frase)

print('')

pivo = "O jogador Shaquile O'Neil foi uma estrela dos Lakers"
print(pivo)
time = 'Os "Lakers" são um time de basquete de Los Angeles'
print(time)
curso = "Tenham bastante atenção ao estudar \"Python\""
print(curso)
barra = 'Escapando com \\'
print(barra)

print('')
print('***************************************************************************************************')
print('')

nome = 'Lucas'
idade = 17
print('O meu nome é %s' %nome)
print('Eu tenho %d anos' %idade)
print('Meu nome é ' + nome + ' e eu tenho ' + str(idade) + ' anos de idade.')

print('')

raio = 30.49358
print('Formatando decimais: %f'%raio)
print('Formatando decimais: %.1f'%raio)
print('Formatando decimais: %.2f'%raio)
print('Formatando decimais: %.3f'%raio)


