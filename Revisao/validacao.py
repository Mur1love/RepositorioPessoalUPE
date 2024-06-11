while True:
    while True:
        nome = input('Digite o seu nome: ')
        if len(nome) < 3:
            print("Nome inválido. Precisa ter mais de 3 caracteres.")
        else: break
    
    while True:
        idade = int(input("Digite a sua idade: "))
        if idade > 150 or idade < 1:
            print("Idade Iválida. Precisa estar entre 0 e 150.")
        else: break

    while True:
        salario = float(input("Digite o seu salario: "))
        if salario < 0:
            print("Salario Iválido. Precisa ser maior que 0.")
        else: break

    while True:
        sexo = input("Digite a sua sexualidade: ")
        if not sexo == "f" and not sexo == "m":
            print("Sexo inválido. Precisa ser feminino (f) ou masculino (m).")
        else: break
    
    while True:
        estado_civil = input("Digite o seu estado civil: ")
        if estado_civil != "c" and estado_civil != "s" and estado_civil != "v" and estado_civil != "d":
            print("Estado Civil inválido. Precisa ser s, c, v ou d")
        else: break

    break

print("Nome: ", nome)
print("Idade: ", idade)
print("Salario: ",salario)
print("Sexo: ",sexo)
print("Estado Civil: ", estado_civil)
