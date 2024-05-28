altura = float(input("Digite a sua altura: "))
peso = float(input("Digite o seu peso: "))

imc = peso / (altura**2)

if imc <= 18.5:
    print("Baixo Peso")
elif imc <= 24.9:
    print("Peso Normal")
elif imc <= 29.9:
    print("Sobrepeso")
elif imc <= 34.9:
    print("Obesidade I")
elif imc <= 39.9:
    print("Obesidade II")
else:
    print("Obesidade III")
