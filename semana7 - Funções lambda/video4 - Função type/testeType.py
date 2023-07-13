print(type('IFSP'))
print(type(835))
print(type(32.9087))
print(type(True))
print(type((1,)))
print(type([]))
print(type({}))
print(type(lambda x:1))
print(type(type('')))

print('')

a = "'Estudar na Rocketseat'"
print('a = ' + a + ' --> ' + str(type(a)))

b = 2022
print('b = ' + str(b) + ' --> ' + str(type(b)))

c = 5.21
print('c = ' + str(c) + ' --> ' + str(type(c)))

d = True
print('d = ' + str(d) + ' --> ' + str(type(d)))

e = ('w', 2, 0.1, not(d))
print('e = ' + str(e) + ' --> ' + str(type(e)))

f = [1, 2, 3]
print('f = ' + str(f) + ' --> ' + str(type(f)))

g = {'nome': 'Lucas', 'idade': 17, 'peso': 61.2, 'adulto': False}
print('g = ' + str(g) + ' --> ' + str(type(g)))

h = lambda x,y: x * y
print('h = ' + str(h) + ' --> ' + str(type(h)))

i = type(h)
print('i = ' + str(i) + ' --> ' + str(type(i)))