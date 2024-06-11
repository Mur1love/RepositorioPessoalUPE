# Faça um programa que leia um número indeterminado de valores, correspondentes a notas, 
# encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). 
# Após esta entrada de dados, faça:
# {X} Mostre a quantidade de valores que foram lidos;
# {X} Exiba todos os valores na ordem em que foram informados;
# {X} Exiba todos os valores na ordem inversa à que foram informados;
# {X} Calcule e mostre a soma dos valores;
# {X} Calcule e mostre a média dos valores;
# {X} Calcule e mostre a quantidade de valores acima da média calculada;
# {X} Calcule e mostre a quantidade de valores abaixo de sete;
# {X} Encerre o programa com uma mensagem;


lista = []

num = 0
i = 0

print('Digite quantas notas você quiser.')
print("Para encerrar digite '-1'")

while num != -1:
    num = float(input('Digite as notas: '))
    lista.append(num)
    i += 1

if lista[-1] == -1:
    print("Programa encerrado.")
    lista.pop()

print("Sua lista de notas: ", lista)

lista_invertida = []
for num in reversed(lista):
    lista_invertida.append(num)

print('Lista invertida: ', lista_invertida)

soma = sum(lista)
print('A soma dos valores: ', soma)

media = soma / len(lista)
print('A média dos valores: ', media)
    
notas_acimas_da_media = []
for num in lista:
    if num >= media:
        notas_acimas_da_media.append(num)

print(notas_acimas_da_media)

notas_abaixo = []
for num in lista:
    if num < 7:
        notas_abaixo.append(num)

print("Notas abaixo de 7: ", notas_abaixo)


