numeros = [5, 1, 2, 7, 9, -1, 4]
numeros2 = [50, 20, 34, 71, 94, 17, 6, 68]


#Descobrir o numero maior
maior = 0
# for i in numeros:
#     if i > maior:
#         maior = i

#Descobre o numero menor
menor = numeros[0]
# for i in numeros:
#     if i < menor:
#         menor = i

#Descobre o menor e o maior no mesmo for

for n in numeros:
    if n > maior:
        maior = n
    if n < menor:
        menor = n


print("O menor numero é: ", menor)
print("O maior numero é: ", maior)


