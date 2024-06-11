# max = int(input("Digite o limite da lista de numeros primos: "))

# primos = []

# for num in range(2, max+1):
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             break
#     else:
#         primos.append(num)

# print(primos)

limite = int(input("Digite o limite superior para a lista de primos: "))
primos = []

for num in range(2, limite + 1):
    é_primo = True 
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            é_primo = False
            break

    if é_primo:
        primos.append(num)

print("Lista de números primos até", limite, ":", primos)





