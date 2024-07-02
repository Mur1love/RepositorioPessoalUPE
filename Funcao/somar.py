def somar(a, b):
    """
    Essa função soma dois números.
    Isso aparece quando se passa o mouse na chamada da função.
    """
    return a + b

# Função sem retorno e sem parametros (PROCEDIMENTO)
def cumprimentar():
    print("Hello, World!")

cumprimentar();

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

print(somar(n1, n2))