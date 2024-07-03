def main():
    #Salvando dicionáros em uma lista (Cadastrando Clientes)
    lista_clientes = []
    for i in range(2):
        dados_cliente = {}
        nome = input("Digite seu nome:")
        dados_cliente['Nome'] = nome
        idade = int(input("Digite sua idade:"))
        dados_cliente['Idade'] = idade

        print(dados_cliente)
        lista_clientes.append(dados_cliente)

    print(lista_clientes)
    

    # for chave, valor in dados_cliente.items():        
    #     print('Chave:', chave, 'Valor:', valor)

    # lista_clientes.append(dados_cliente)
    # print(lista_clientes)



main()

# keys()
# values()
# items()
# keys()
# get()
# keys()