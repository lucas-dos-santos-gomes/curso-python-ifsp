string1 = "Oi pessoal!"
print(string1)

string2 = 'Python IFSP'
print(string2)

print(" ")
print('******************************************************************************************************')
print(' ')

nome = 'Maria José da Silva'
print(nome)
#string -> 0 à infinito
print(nome[0]) #M
print(nome[1]) #a
print(nome[2]) #r
print(nome[3]) #i
print(nome[4]) #a

print(nome[5]) #

print(nome[6]) #J
print(nome[7]) #o
print(nome[8]) #s
print(nome[9]) #é

print(nome[10]) #

print(nome[11]) #d
print(nome[12]) #a

print(nome[13])#

print(nome[14]) #S
print(nome[15]) #i
print(nome[16]) #l
print(nome[17]) #v
print(nome[18]) #a

# print(nome[20]) == erro
print(' ')

print(nome[6:10]) #imprime o valor de uma posição a outra
print(nome[1:10:2]) #imprime o valor das posições 1 até 10, mas pulando 2 caracteres
print(string1[1:10:2])

print(' ')

print(nome[:10]) #imprime do começo até a posição selecionada
print(nome[10:]) #imprime da posição selecionada ate o final
print(nome[::3]) #vai do começo ao fim pulando de 3 em 3

print(" ")
print('******************************************************************************************************')
print(' ')

frase = 'Aprendendo Python com o IFSP'
print(frase)
print(len(frase)) #imprime a quantidade de caracteres da variável selecionada

contador = len(string1)
print(contador) #mesmo processo feito de um jeito diferente

print(" ")
print('******************************************************************************************************')
print(' ')

string1 = string1.replace('pessoal', 'rapaziada') #substitui a parte selecionada pelo que você quiser
print(string1)

frase = frase.replace('IFSP', 'Instituto Federal de São Paulo')
print(frase)

print(" ")
print('******************************************************************************************************')
print(' ')

print(frase)
letra = 'd'
contarLetras = frase.count(letra) #conta quantos caracteres que você escolher possui
print('Existem', contarLetras, "letras '" + letra + "' na frase acima")

acharLetra = frase.find('o') #encontra a posição da primeira letra caso tenha mais de uma
print(acharLetra)

acharPalavra = frase.find('Paulo') #encontra a posição da primeira letra da palavra
print(acharPalavra)

print(frase.find('instituto')) #não será encontrado
print('')
print(frase.split()) #divide a variável por palavras a cada ocorrência de esaço encontrada

print(" ")
print('******************************************************************************************************')
print(' ')

print('Padrão:', frase)
print('')
print('Upper:', frase.upper()) #deixa todas as letras em maiúsculo
print('Lower:', frase.lower()) #deixa todas as letras em minúsculo
print('Capitalize:', frase.capitalize()) #deixa a primeira letra da variável em maiúsculo
print('Title:', frase.title()) #deixa a primeira letra de cada palavra em maiúsculo
print('Swapcase:', frase.swapcase()) #troca tudo que é maiúsculo por minúsculo e vice-versa

print(" ")
print('******************************************************************************************************')
print(' ')

numero = 579
print(numero, type(numero))
numero = str(numero)
print(numero, type(numero))

print(" ")
print('******************************************************************************************************')
print(' ')


