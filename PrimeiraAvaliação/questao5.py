lista_professores = []
lista_alunos = []

print("Bem vindo a lista de Professores e alunos!")

while True:
    print("Menu: ")
    print("1 - Cadastrar novo professor")
    print("2 - Cadastrar novo Aluno")
    print("3 - Ver Professores cadastrados")
    print("4 - Ver Alunos cadastrados")
    print("5 - Excluir último professor da lista")
    print("6 - Excluir último aluno da lista")
    print("7 - Encerrar programa")
    escolha = int(input())

    if escolha == 1:
        while True:
            print("Para voltar digite 0")
            nome_professor = input("Digite o nome do professor: ")
            if nome_professor == "0":
                break
            elif len(nome_professor) < 3:
                print("Professor não cadastrado, o nome deve conter mais de 3 caracteres.")
            else:
                lista_professores.append(nome_professor)
                print("Professor cadastrado com sucesso!")
                break

    elif escolha == 2:
        while True:
            print("Para voltar digite 0")
            nome_aluno = input("Digite o nome do aluno: ")
            if nome_aluno == "0":
                break
            elif len(nome_aluno) < 3:
                print("Aluno não cadastrado, o nome deve conter mais de 3 caracteres.")
            else:
                lista_alunos.append(nome_aluno)
                print("Aluno cadastrado com sucesso!")
                break

    elif escolha == 3:
        if len(lista_professores) == 0:
            print("Ainda não tem professores cadastrados")
        else:
            print("Os Professores cadastrados são: ")
            print(lista_professores)

    elif escolha == 4:
        if len(lista_alunos) == 0:
            print("Ainda não tem alunos cadastrados são:")
        else:
            print("Os Alunos cadastrados: ")
            print(lista_alunos)

    elif escolha == 5:
        if len(lista_professores) == 0:
            print("Ainda não tem professores cadastrados")
        else:
            print(f"O professor {lista_professores.pop()} foi retirado da lista")

    elif escolha == 6:
        if len(lista_alunos) == 0:
            print("Ainda não tem alunos cadastrados")
        else:
            print(f"O aluno {lista_alunos.pop()} foi retirado da lista")

    elif escolha == 7:
        print("O sistema está chegando ao fim...")
        print(f"Ao final, tivemos {len(lista_professores)} professores cadastrados \n e {len(lista_alunos)} alunos cadastrados.")
        print("Até a proxima. Tchau.")
        break


            







