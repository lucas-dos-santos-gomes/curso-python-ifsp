print(().__sizeof__())
print([].__sizeof__())

print()

notas = ('MB',)
print(notas)
print(type(notas))

#notas.append('B-') --> erro

notas += ('I',)
print(notas)

print()

x = 0
minha_tupla = ([1,2,3], x, ['a','b'])
print(minha_tupla)

x = 'Curso'
minha_tupla[2].append('c')
print(minha_tupla)

#minha_tupla[1] = 'Python' --> erro

print()

from collections import namedtuple

filme = namedtuple('filme', ['Marvel', 'DC', 'Disney', 'Dreamworks'])
filmeFav = filme('Ultimato', 'Aquaman', 'Zootopia', 'Kung Fu Panda')
print(filmeFav, filmeFav[1])
print(filmeFav[0])
print(filmeFav.Disney)

print(type(filmeFav))