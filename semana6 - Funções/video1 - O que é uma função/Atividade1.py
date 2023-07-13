#Faça um algoritmo que solicite ao usuário números e os armazene em um vetor de 10 posições.
#Crie uma função que recebe o vetor preenchido e substitua os valores positivos por 1 e os neativos por 0.

contador = 1
print('')

# 1- criando a função
def binario(vet):
    for i in range(10):
        if vet[i] >= 0:
            vet[i] = 1
        else:
            vet[i] = 0
    return vet

# 2- construindo o vetor (array)
vet = [0] * 10
for i in range(10):
    vet[i] = int(input('Digite um valor (' + str(contador) + '): '))
    contador += 1
else:
    print('')
print('Vetor:')
print(vet)
print('')

# 3- chamando a função
binario(vet)
print('Função:')
print(vet)

print('')
print('Fim da aplicação')
