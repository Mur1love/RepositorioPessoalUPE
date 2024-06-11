precos = {
    "File Duplo": [4.9, 5.8],
    "Alcatra": [5.9, 6.8],
    "Picanha": [6.9, 7.8]
}

print("Tipos de carne: File Duplo, Alcatra, Picanha")
tipo = input("Digite o tipo de carne que você quer comprar: ")
qtd = float(input("Digite a quantidade de carne em KG: "))
pagamento = input("Vai pagar com cartão? (s/n): ")

if tipo in precos:
    if qtd <= 5:
        preco_total = precos[tipo][0] * qtd
    else:
        preco_total = precos[tipo][1] * qtd

    if pagamento == 's':
        desconto = preco_total * 0.05
    else:
        desconto = 0

valor_a_pagar = preco_total - desconto


print("Cupom Fiscal")
print("Tipo de carne:", tipo)
print("Quantidade de carne:", qtd, "Kg")
print("Preço total: R$", preco_total)
if pagamento.lower() == 's':
    print("Tipo de pagamento: Cartão")
else:
    print("Tipo de pagamento: Dinheiro")
print("Valor do desconto: R$", desconto)