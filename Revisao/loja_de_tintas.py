import math

area_metros_quadrados = float(input("Informe a área a ser pintada (em metros quadrados): "))
cobertura_tinta_litros_metro_quadrado = 1 / 6   
fator_folga = 1.1 

tinta_necessaria_litros = area_metros_quadrados * cobertura_tinta_litros_metro_quadrado * fator_folga
print("Tinta necessaria em litros: ", math.ceil(tinta_necessaria_litros))

#Descobre quantas latas precisa
quantidade_latas = math.ceil(tinta_necessaria_litros / 18)
preco_latas = quantidade_latas * 80

print("Latas de 18 litros:")
print(f"Quantidade: {quantidade_latas} latas")
print(f"Preço total: R$ {preco_latas:.2f}")

#Descobre quantos galoes precisam
quantidade_galoes = math.ceil(tinta_necessaria_litros / 3.6)
preco_galoes = quantidade_galoes * 25.00


print("\nGalões de 3,6 litros:")
print(f"Quantidade: {quantidade_galoes} galões")
print(f"Preço total: R$ {preco_galoes:.2f}")

#Melhor opção entre latas e galões
melhor_quantidade_galoes = 0
melhor_quantidade_latas = 0
melhor_preco = max(quantidade_galoes * 25.00 + quantidade_latas * 80.00, 0)

for quantidade_galoes_simulacao in range(quantidade_galoes + 1):
    tinta_restante_simulacao = tinta_necessaria_litros - quantidade_galoes_simulacao * 3.6
    quantidade_latas_simulacao = math.ceil(tinta_restante_simulacao / 18)
    preco_simulacao = quantidade_galoes_simulacao * 25.00 + quantidade_latas_simulacao * 80.00
    if preco_simulacao < melhor_preco:
        melhor_quantidade_galoes = quantidade_galoes_simulacao
        melhor_quantidade_latas = quantidade_latas_simulacao
        melhor_preco = preco_simulacao

print("\n Combinação mais economica (Latas e Galões):")
print(f"Quantidade de galões: {melhor_quantidade_galoes} galões")
print(f"Quantidade de latas: {melhor_quantidade_latas} latas")
print(f"Preço total: R$ {melhor_preco:.2f}")

