continuar = True

while continuar:
    nota = float(input("Digite uma nota: "))

    if nota >= 0 and nota <= 10:
        print("Nota Válida!")
        continuar = False
    else:
        print("Nota Iválida!")
