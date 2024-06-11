lista_de_perguntas = [
    "Telefonou para a vítima?", 
    "Esteve no local do crime?", 
    "Mora perto da vítima?", 
    "Devia para a vítima?", 
    "Já trabalhou com a vítima?"           
]

respostas = []

for pergunta in lista_de_perguntas:
    print(pergunta)
    print("1 - SIM ou 0 - NAO")
    resposta = int(input())
    respostas.append(resposta)

if respostas.count(1) == 2:
    print("Classificação: SUSPEITO")
elif respostas.count(1) == 3 or respostas.count(1) == 4:
    print("Classificação: CUMPLICE")
elif respostas.count(1) == 5:
    print("Classificação: ASSASSINO")
else:
    print("Classificação: INOCENTE")