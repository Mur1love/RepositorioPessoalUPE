lista = []

for i in range(5):
    num = int(input("Digite um numero: "))
    lista.append(num)

print(lista)

print(f"A soma dos valores é: {sum(lista)}, e a média é: {sum(lista) / 5}")
