n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digite a nota 3: "))


media = (n1 + n2 + n3) / 3

if media >= 7:
    print(f"Nota: {media}")
    print("Aluno aprovado por média!")
else:
    nota_faltante = 7 - media
    print(f"Nota: {media}")
    print("Aluno na prova final")
    print(f"Ele precisa de {nota_faltante} para passar!")
