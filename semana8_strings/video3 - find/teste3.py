frase = 'Indicar o ponto de início da busca'
palavra = 'Indicar'
result = frase.find(palavra, 10)
print(result)

palavra = 'ponto'
result = frase.find(palavra, 5, 15)
print(result)

print()

frase = 'Passando o parâmetro, o inicio e o fim.'
print(frase)
busca = input('Informe a palavra ou o caractere que deseja buscar: ')
inicio = int(input('Informe a posição inicial de busca: '))
fim = int(input('Informe a posição final de busca: '))
print(frase.find(busca,inicio,fim))