# Questão 6:
num_inicial = int(input("Digite o numero inicial: "))
num_final = int(input("Digite o numero final: "))

lista = []

for i in range(num_inicial, num_final + 1):
    lista.append(i)

print(lista)


# Questão 7:
print("A soma dos números é: ", sum(lista))
