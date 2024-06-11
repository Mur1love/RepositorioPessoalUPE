valor_hora = float(input('Digite quanto você ganha por hora: '))
horas = float(input('Digite quantas horas você trabalhou esse mês: '))

salario_bruto = valor_hora * horas
print(salario_bruto)

imposto_renda = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - (inss + sindicato + imposto_renda)

print('Salario Bruto: R$', salario_bruto)
print('IR (11%): R$', imposto_renda)
print('INSS (8%): R$', inss)
print('Sindicato (5%): R$', sindicato)
print('Salario Liquido: R$', salario_liquido)
