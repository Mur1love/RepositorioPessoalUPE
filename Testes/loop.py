# for i in range(5):
#     print('Seja bem vindo ao LOOP')


tecla = ""
while tecla != "s":
    print("Bem vindo ao meu Programa!")
    print("Menu:")
    print("a - Agradecer.")
    print("p - Pedir ajuda.")
    print("s - sair.")
    tecla = input()

    if tecla == "a":
        print("Obrigado!")
    elif tecla == "p":
        print("Socorro!")
    elif tecla == "s":
        print("Saindo do Programa.")
    else:
        print("Insira uma tecla válida!")
