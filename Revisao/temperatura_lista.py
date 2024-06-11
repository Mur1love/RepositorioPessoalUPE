temperaturas = []

temperatura = float(input('Digite algumas temperaturas (Para sair digite 999): '))
while temperatura != 999.0:
    temperaturas.append(temperatura)
    temperatura = float(input('Digite algumas temperaturas (Para sair digite 999): '))

print(temperaturas)

print(min(temperaturas))
print(max(temperaturas))
print(sum(temperaturas) / len(temperaturas))