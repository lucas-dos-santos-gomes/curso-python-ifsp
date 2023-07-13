#Possuir no mínimo 10 centímetro em cada mecha;
#ter atenção para que os fios cortados não caiam no chão;
#Não ter nenhuma doença capilar;
#Guardar os fios secos e limpos em um saco plástico

continuar = input('Deseja iniciar o sistema? (S/N): ').upper().strip()
while continuar != 'S' and continuar != 'N':
    print('Opção inválida')
    continuar = input('Digite S - (Sim) ou N - (Não): ').upper().strip()
print()

totalDoadores = 0
totalMasculino = 0
totalFeminino = 0
doacoesPerdidas = 0

while continuar == 'S':
    totalDoadores += 1
    nome = input('Informe seu nome: ').title().strip()

    sexo = input('Informe o seu sexo (M/F): ').upper().strip()
    while sexo != 'M' and sexo != 'F':
        print('Opção inválida')
        sexo = input('Digite M (Masculino) ou F (Feminino): ').upper().strip()
    print()

    #Doadores por sexo
    if sexo == 'M':
        totalMasculino += 1
    else:
        totalFeminino += 1

    #Teste: tamanho da mecha
    tamanhoMecha = int(input('Qual o tamanho da mecha de cabelo em cm? '))
    if tamanhoMecha < 10:
        print('Para a doação, a mecha deve possuir no mínimo 10 cm')
        print('Deixe seu cabelo crescer mais um pouco')
        print()
        doacoesPerdidas += 1
    else:
        chao = input('Durante o processo, a mecha de cabelo caiu no chão? (S/N): ').upper().strip()
        while chao != 'N' and chao != 'S':
            print('Opção inválida')
            chao = input('Digite S (Sim) ou N (Não)').upper().strip()

        #Teste: se a mecha caiu no chão
        if chao == 'S':
            print('Para a doação, a mecha não pode cair ou tocar no chão')
            print()
            doacoesPerdidas += 1
        else:
            doencaCapilar = ('O doador possui alguma doença capilar? (S/N): ').upper().strip()
            while doencaCapilar != 'S' and doencaCapilar != 'N':
                print('Opção inválida')
                doencaCapilar = input('Digite S (Sim) ou N (Não): ').upper().strip()

            #Teste: doença capilar
            if doencaCapilar == 'S':
                print('Para a doação, os cabelos devem estar saudáveis')
                print()
                doacoesPerdidas += 1
            else:
                armazenamento = input('A mecha foi armazenada adequadamente? (S/N): ').upper().strip()
                while armazenamento != 'S' and armazenamento != 'N':
                    print('Opção inválida')
                    armazenamento = input('Digite S (Sim) ou N (Não): ').upper().strip()

                #Teste: armazenamento
                if armazenamento == 'N':
                    print('Para a doação, os cabelos devem ser guardados limpos e secos em um saco plástico')
                    print()
                    doacoesPerdidas += 1

    continuar = input('Deseja cadastrar uma nova doação? (S/N): ').upper().strip()
    while continuar != 'S' and continuar != 'N':
        print('Opção inválida')
        continuar = input('Digite S (Sim) ou N (Não): ').upper().strip()
else:
    print('\n\n' + ' Apresentar os resultados finais '.center(60,'-') + '\n\n')

print(f'Total de doações: {totalDoadores}')
print(f'Total de doações perdidas: {doacoesPerdidas}')
print(f'Total de doações válidas: {totalDoadores - doacoesPerdidas}')
print()
print(f'Porcentagem de participantes do sexo feminino: {(totalFeminino * 100) / totalDoadores}%')
print(f'Porcentagem de participantes do sexo masculino: {(totalMasculino * 100) / totalDoadores}%')