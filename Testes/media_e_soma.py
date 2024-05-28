soma = 0
qtd = int(input('Digite a quatidade de numeros: '))
for i in range(qtd):
    num = float(input(f'digite o {i+1} numero: ')) 
    soma = soma + num

media = soma / qtd

print(f'A soma dos números é {soma}.')
print(f'A média dos números é {media}.')



