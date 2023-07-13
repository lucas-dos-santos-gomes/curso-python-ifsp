#Percorra os valores de uma lista e eleve-os ao quadrado, depois, é retornado o dobro deles com a operação x*2.
#Como a operação irá nos retornar um map object, utilize o método list para voltar a ter um array.

lista = []
#ou
lista = list()

num = int(input('Informe um número para a lista: '))
lista.append(num)
print('Lista ' + str(lista))
continuar = input('Deseja inserir mais um número? (S/N): ').upper()
while continuar != 'S' and continuar != 'N':
    continuar = input("Resposta incorreta. Digite 'S' (Sim) ou 'N' (Não): ").upper()

print()

while continuar == 'S':
    num = int(input('Informe outro número para a lista: '))
    lista.append(num)
    print('Lista ' + str(lista))
    continuar = input('Deseja inserir mais um número? (S/N): ').upper()
    while continuar != 'S' and continuar != 'N':
        continuar = input("Resposta incorreta. Digite 'S' (Sim) ou 'N' (Não): ").upper()
    print()
else:
    elev = list(map(lambda x: x**2, lista))
    dobr = list(map(lambda x: x*2, elev))
print('Lista ' + str(dobr))