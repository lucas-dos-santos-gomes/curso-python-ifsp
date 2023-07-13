frase = 'Python é uma das 10 linguagens mais usadas no mundo!'
print(frase)
busca = input('Informe uma palavra que deseja localizar na frase: ')
resultado = frase.find(busca)
print()
print('Posição: ' + str(resultado))