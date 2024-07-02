
#Jeito que eu fiz.
def imprimir_linhas(n_max, numeros):
    for n in numeros:
        print()
        for j in range(n):
            print(n, end=' ') #end = ' 'escreve na mesma linha

#Jeito que o professor fez (melhor)
def criar_arvore_numeros(n):
    for i in range(1, n + 1):
        for j in range(1):
            print(i, end = " ")
        print()

def main():
    n_max = int(input("Digite um numero: "))
    numeros = []
    for n in range(1, n_max+1):
        numeros.append(n)
    
    imprimir_linhas(n_max, numeros)

if __name__ == "__main__":
    main()