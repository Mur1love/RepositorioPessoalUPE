horas = float(input("Digite o numero de horas trabalhadas: "))


if horas <= 50:
    salario = horas * 10
    print("Salário: R$", salario)
else:
    horas_extras = horas - 50
    valor_hora_extra = horas_extras * 20
    salario_com_hora_extra = 500 + valor_hora_extra
    print("Salário com hora extra: R$", salario_com_hora_extra)
