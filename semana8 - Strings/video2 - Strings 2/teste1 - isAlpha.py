print('-' * 10 + ' is Alpha ' + '-' * 10)

endereco = 'Av Paulista'
print('Av Paulista = ' + str(endereco.isalpha()))

endereco = 'Av. Paulista, 427'
print('Av. Paulista, 427 = ' + str(endereco.isalpha()))

sobrenome = "Gomes"
print("Gomes = " + str(sobrenome.isalpha()))

especiais = '#$)@*'
print('#$)@* = ' + str(especiais.isalpha()))

print()
print('-' * 10 + ' is Alnum ' + '-' * 10)

num = '2'
print('2 = ' + str(num.isalnum()))

num = '9436'
print('9436 = ' + str(num.isalnum()))

num = '10 100 1000'
print('10 100 1000 = ' + str(num.isalnum()))

dec = '21.9'
print('21.9 = ' + str(num.isalnum()))

print()
print('-' * 10 + ' is Space ' + '-' * 10)

espaco = ''
print("'' = " + str(espaco.isspace()))

espaco = ' '
print("' ' = " + str(espaco.isspace()))

espaco = '     '
print("'     ' = " + str(espaco.isspace()))

espaco = 'Lucas Gomes'
print("Lucas' 'Gomes = " + str(espaco[5].isspace()))

print()
print('-' * 10 + ' is Lower ' + '-' * 10)

word = 'Joao Nunes'
print('Joao Nunes = ' + str(word.islower()))

word = 'joao nunes'
print('joao nunes = ' + str(word.islower()))

word = '17'
print('17 = ' + str(word.islower()))

word = '17 anos de idade'
print('17 anos de idade = ' + str(word.islower()))

print()
print('-' * 10 + ' is Decimal ' + '-' * 10)

dec = '19.7'
print('19.7 = ' + str(dec.isdecimal()))
print("19.'7' = " + str(dec[3].isdecimal()))
print("19'.'7 = " + str(dec[2].isdecimal()))
dec = '3.1416'
print("3.'1416' = " + str(dec[2:5].isdecimal()))
print("'3'.'1' 4 '1' 6 = " + str(dec[::2].isdecimal()))