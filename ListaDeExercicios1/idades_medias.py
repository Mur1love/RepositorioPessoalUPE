qtd_pessoas = int(input("Digite a quantidade de pessoas: "))

lista_de_idades = []

for i in range(qtd_pessoas):
    idades = int(input("Digite as idades dessas pessoas: "))
    lista_de_idades.append(idades)

print(lista_de_idades)

media = sum(lista_de_idades) // qtd_pessoas

print("Média: ", media)

if media <= 25:
    print("Turma Jovem.")
elif media <= 60:
    print("Turma Adulta.")
else:
    print("Turma Idosa.")
