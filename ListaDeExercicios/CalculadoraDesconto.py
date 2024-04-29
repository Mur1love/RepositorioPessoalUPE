valor = float(input('Digite o valor do produto: '))
porcentagem = int(input('Digite o desconto em %: '))

desconto = (valor / 100) * porcentagem

valor_com_desconto = valor - desconto

print('O seu produto de R$', valor, 'recebeu um desconto de', porcentagem, '%', 'e agora você leva por R$', valor_com_desconto,'!' )