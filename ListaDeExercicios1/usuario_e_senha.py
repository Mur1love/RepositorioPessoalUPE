nome = input("Digite o seu nome de usuário: ")

while True:
    senha = input("Digite a sua senha: ")
    if senha == nome:
        print("Senha igual o nome de Usuário. Tente uma senha diferente.")
    else:
        print("Usuário criado com sucesso!")
        break
