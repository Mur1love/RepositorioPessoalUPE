valor_em_reais = float(input('Digite o valor em R$: '))
cotacao_dolar = float(input('Digite a cotação do USD: '))

valor_convertido = valor_em_reais / cotacao_dolar

print('R$', valor_em_reais, "em Dólar Americano equivale a USD", valor_convertido)
