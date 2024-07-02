
def calcular_fatorial(n):
    if n == 0:
        return 1
    else: 
        return n * calcular_fatorial(n - 1)
    
    # def fatorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fatorial(n - 1)

# print(fatorial(n))


def main():

    n = int(input("Digite um número: "))

    calcular_fatorial(n)

if __name__ == "__main__":
    main()