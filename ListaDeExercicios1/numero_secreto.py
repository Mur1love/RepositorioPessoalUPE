import random

randon_num = random.randint(1, 10)

print("Tente adivinha o numero secreto:")

while True:
    num = int(input())
    if num > randon_num:
        print("O numero secreto é menor!")
    elif num < randon_num:
        print("O numero secreto é maior!")
    elif num == randon_num:
        print("ACERTOU!")
        break
    else:
        print("Valor Inválido!")
