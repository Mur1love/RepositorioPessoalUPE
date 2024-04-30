
adicionando = int(input('Digite um número para ver sua tabuada: '))

print("A tabuada de soma do", adicionando, "é: ")

for i in range(1 , 11): 
    print(f"{adicionando} + {i} = {adicionando + i}")