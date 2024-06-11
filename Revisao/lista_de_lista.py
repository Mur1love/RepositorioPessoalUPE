# for i in range(3):
#     for j in range(3):
#         print(i, j)

lista_idades = []

for j in range(2):
    n = int(input('Digite a quantidade de idades que você deseja digitar: '))
    lista_temp = []
    for i in range(n):
        idade = int(input(f'Digite a {i+1}ª idade: '))
        lista_temp.append(idade)
    lista_idades.append(lista_temp)

print(lista_idades)

print("Elementos com o FOR:")
for idade in lista_idades:
    print(idade)

print("Elementos com o WHILE:")
contador = 0
while contador < len(lista_idades):
    print(lista_idades[contador])
    contador += 1