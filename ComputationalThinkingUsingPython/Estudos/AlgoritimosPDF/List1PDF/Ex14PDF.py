""" ___________________________________________________________________________________________________________________________________
14 - Crie um algoritmo para calcular o pagamento de comissão de vendedores de peças, levando em consideração que sua comissão será de 
5% do total da venda e que você tem os seguintes dados:nn

- identificação do vendedor
- código da peça
- preço unitário da peça
- quantidade vendida

O algoritmo deve imprimir a identificação do vendedor, o total vendido pelo
vendedor e o valor da comissão da venda.

(Entrada)
- 

(Processamento)
- 

(Saída)
- 

"""

print('\nAlgorítimo: Comissão de 5%\n')

id = int(input('Digite o ID do vendedor: '))
cd = int(input('Digite o código da peça: '))
pr = float(input('Digite o valor da peça: R$'))
qt = int(input('Digite a quantidade de peças: '))

tv = pr * qt
cm = tv * (5/100)

print(f'\n- ID do vendedor:{id}\n- Total de peças de código ({cd}) vendidas: R${tv:.2f}\n- Comissão da venda (5%): R${cm:.2f}\n')

























"""
# Entrada
print('\nAlgorítimo: Comissão\n')

nomevendedor = str(input('Digite seu nome: '))
codigopeca = str(input('Digite o código da peça: '))
valorpeca = float(input('Digite o valor da peça: R$'))
quantidadepeca = int(input('Quantas peças foram vendidas? : '))

# Processamento
valorvenda = valorpeca*quantidadepeca
valorcomissao = valorvenda*(5/100)

# Saída
print(f'\nAs vendas da peça ID {codigopeca} renderam: R${valorvenda:.2f}\n{nomevendedor}, você receberá R${valorcomissao:.2f} de comissão.\n')
"""
