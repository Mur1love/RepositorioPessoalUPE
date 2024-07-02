def calcular_media(n1, n2, n3):
    soma = n1 + n2 + n3
    return soma / 3

def main():

    n1 = float(input("Digite o primero numero: "))
    n2 = float(input("Digite o primero numero: "))
    n3 = float(input("Digite o primero numero: "))

    print("A média é igual a: ", calcular_media(n1, n2, n3))


if __name__ == "__main__":
    main()



