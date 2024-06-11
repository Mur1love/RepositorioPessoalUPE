numeros = []
impares = []
pares = []
for num in range(20):
    numeros.append(int(input()))

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
        
print(numeros)

print('Numeros pares: ', pares)
print('Numeros Impares: ', impares)