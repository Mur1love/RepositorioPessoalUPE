
# n = int(input("Digite um numero: "))

# def fatorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fatorial(n - 1)

# print(fatorial(n))

n = int(input("Digite um numero: "))

resultado = 1
for i in range(n, 0, -1):
    resultado *= i

print(f"O fatorial de {n} é {resultado}.")