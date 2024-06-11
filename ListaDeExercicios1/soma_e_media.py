lista = []

for i in range(5):
    num = int(input("Digite um numero: "))
    lista.append(num)

print(lista)

# soma = 0
# for i in lista:
#     soma += i

# media = soma / len(lista)

# print(soma)
# print(media)

print(f"A soma dos valores é: {sum(lista)}, e a média é: {sum(lista) / len(lista)}")
