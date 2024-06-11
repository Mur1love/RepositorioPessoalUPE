import random

lista_de_valores = []

for i in range(100):
    valor_dado = random.randint(1, 6)
    lista_de_valores.append(valor_dado)

print(lista_de_valores)
print("Quantidade de 1s: ", lista_de_valores.count(1))
print("Quantidade de 2s: ", lista_de_valores.count(2))
print("Quantidade de 3s: ", lista_de_valores.count(3))
print("Quantidade de 4s: ", lista_de_valores.count(4))
print("Quantidade de 5s: ", lista_de_valores.count(5))
print("Quantidade de 6s: ", lista_de_valores.count(6))

# lista_de_uns = []
# lista_de_dois = []
# lista_de_tres = []
# lista_de_quatro = []
# lista_de_cinco = []
# lista_de_seis = []


# for n in lista_de_valores:
#     if n == 1:
#         lista_de_uns.append(n)
    
