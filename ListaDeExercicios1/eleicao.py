qtd_eleitores = int(input("Digite a quantidade de eleitores: "))
votos = [0, 0, 0]

for i in range(qtd_eleitores):
    voto = int(input("Digite o seu voto: 1, 2 ou 3: "))
    while voto < 1 or voto > 3:
        print("Voto Invalido. Deve ser entre 1, 2 ou 3.")
        voto = int(input("Digite o seu voto: 1, 2 ou 3: "))
    votos[voto - 1] += 1

print("Resultado das eleições: ")
print(f"Candidato 1: {votos[0]} votos")
print(f"Candidato 2: {votos[1]} votos")
print(f"Candidato 3: {votos[2]} votos")
