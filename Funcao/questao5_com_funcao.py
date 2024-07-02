#from nome_do_arquivo import * --> importa tudo
#from nome_do_arquivo import nome_da_funcao... --> importa uma funcao definida

def menu():
    """
    Imprime o menu com as opções enumerada.
    """
    print("Menu: ")
    print("1 - Cadastrar novo professor")
    print("2 - Cadastrar novo Aluno")
    print("3 - Ver Professores cadastrados")
    print("4 - Ver Alunos cadastrados")
    print("5 - Excluir último professor da lista")
    print("6 - Excluir último aluno da lista")
    print("7 - Encerrar programa")

def cadastrar_professor(lista_professores):
    """
    Recebe uma lista como parametro.
    Checa se o nome do professor contém menos que 3 caracteres.
    Guarda o nome do professor na lista.
    """
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
    return lista_professores
    
def cadastrar_aluno(lista_alunos):
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
    return lista_alunos

def listar_professores(lista_professores: list):
    if len(lista_professores) == 0:
        print("Ainda não tem professores cadastrados")
    else:
        print("Os Professores cadastrados são: ")
        print(lista_professores)

def listar_alunos(lista_alunos):
    if len(lista_alunos) == 0:
        print("Ainda não tem alunos cadastrados:")
    else:
        print("Os Alunos cadastrados: ")
        print(lista_alunos)
    
def excluir_ultimo_professor(lista_professores):
    if len(lista_professores) == 0:
        print("Ainda não tem professores cadastrados")
    else:
        print(f"O professor {lista_professores.pop()} foi retirado da lista")

def excluir_ultimo_aluno(lista_alunos):
    if len(lista_alunos) == 0:
        print("Ainda não tem alunos cadastrados")
    else:
        print(f"O aluno {lista_alunos.pop()} foi retirado da lista")

def finalizar_programa(lista_professores, lista_alunos): 
    print("O sistema está chegando ao fim...")
    print(f"Ao final, tivemos {len(lista_professores)} professores cadastrados \n e {len(lista_alunos)} alunos cadastrados.")
    print("Até a proxima. Tchau.")

def main(): 

    lista_professores = []
    lista_alunos = []

    print("Bem vindo a lista de Professores e alunos!")

    while True:
        menu()
        escolha = int(input())

        if escolha == 1:
            lista_professores = cadastrar_professor(lista_professores)
                
        elif escolha == 2:
            lista_alunos = cadastrar_aluno(lista_professores)

        elif escolha == 3:
            listar_professores(lista_professores)

        elif escolha == 4:
            listar_professores(lista_alunos)

        elif escolha == 5:
            excluir_ultimo_professor(lista_professores)

        elif escolha == 6:
            excluir_ultimo_aluno(lista_alunos)

        elif escolha == 7:
            finalizar_programa(lista_professores, lista_alunos)
            break

if __name__ == "__main__":
    main()


            







