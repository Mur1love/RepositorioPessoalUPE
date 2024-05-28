indice_poluicao = float(input("Digite o Indice de Puluição: "))

if indice_poluicao >= 0.3 and indice_poluicao < 0.4:
    print("Intimar indústrias do 1 grupo.")
elif indice_poluicao >= 0.4 and indice_poluicao < 0.5:
    print("Intimar indústrias do 1 e 2 grupo.")
elif indice_poluicao >= 0.5:
    print("Intimar indústrias do 1, 2 e 3 grupo.")
else:
    print("Indice de poluição aceitável.")
