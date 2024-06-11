n = int(input("Quantos termos você quer mostrar? "))

n1 = 0
n2 = 1 

lista_fibo = [n1, n2]

i = 0 
while i <= n:
    n3 = n1 + n2
    lista_fibo.append(n3)
    n1 = n2 
    n2 = n3
    i += 1

print(lista_fibo)