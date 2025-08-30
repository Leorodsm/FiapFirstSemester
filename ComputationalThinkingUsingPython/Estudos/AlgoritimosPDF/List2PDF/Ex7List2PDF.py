"""
Crie um programa que receba como entrada o
crédito e depois o preço de itens comprados
por esse cliente. O programa deverá parar
de solicitar novos preços quando o crédito
disponível for insuficiente para pagar por
um deles. Ao final exiba o total da compra
e o crédito restante.

"""

credito = float(input("\nDigite seu crédito atual: R$"))
preco = float(input("Digite o preço do produto: R$ "))

total = 0

while credito >= preco:
    total = total + preco
    credito = credito - preco

    print(f'\n- Total: R${total:.2f} -Credito: R${credito:.2f}')

    preco = float(input("\nDigite o preço do produto: R$"))

print(f'\n- Total da compra: R${total:.2f}\n- Credito restante: R${credito:.2f}\n')





