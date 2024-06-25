n = int(input("Digite um numero: "))

fatorial = 1
for i in range(n, 0, -1):
    fatorial = fatorial * i

print(fatorial)