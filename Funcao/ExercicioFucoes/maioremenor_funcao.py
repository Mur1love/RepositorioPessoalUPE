
def main():
    lista = [4, 5, 7, 2, 10, 12]

    print("O maior e o menor número respectivamente",descobrir_maior_e_menor(lista))


def descobrir_maior_e_menor(numeros):
    maior = 0
    menor = numeros[0]
            
    for n in numeros:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    return maior, menor

if __name__ == "__main__":
    main()