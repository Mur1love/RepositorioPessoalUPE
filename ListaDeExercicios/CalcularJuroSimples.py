capitalInicial = float(input('Digite o valor inicial: '))
porcentagem = int(input('Digite a taxa de juros ao ano: '))
tempo = int(input('Digite o tempo em anos: '))

taxa = porcentagem / 100

juros = capitalInicial * taxa * tempo

montante = juros + capitalInicial

print('O montante equivale a R$', montante, '!')
