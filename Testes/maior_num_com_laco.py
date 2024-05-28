maior = 0
for i in range(5):
    num = int(input(f'Digite o {i+1} numero: '))
    if num >= maior: 
        maior = num

print(f'O maior numero é {maior}')

