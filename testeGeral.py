print('')
frase = 'O rato roeu a roupa do rei de Roma'
print(frase)
print('')
letra = input('Qual letra você deseja procurar na frase? ')
print(letra)

print(" ")
print('******************************************************************************************************')
print(' ')

contarLetras = frase.count(letra)
if(contarLetras <= 1):
    print('Existe', contarLetras, "letra '" + letra + "' na frase acima")
else:
    print('Existem', contarLetras, "letras '" + letra + "' na frase acima")





