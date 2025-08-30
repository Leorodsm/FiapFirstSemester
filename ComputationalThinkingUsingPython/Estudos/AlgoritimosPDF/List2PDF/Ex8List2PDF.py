"""
Variável Flag:

Ela é do tipo booleano, ou seja, "Verdadeira: true" ou "Falsa: false". Com ela, é possível iniciar o laço sem 
uma varíavel para comparar. Se ela for "Falsa: false" o laço de repetição se encerra

"""

total = 0
quero_comprar = True

while quero_comprar:
    preco = float(input('Preço: '))
    total += preco
    opcao = input('Continuar comprando (s/n)? ')

    if opcao != 's':
        quero_comprar = False
    
print(f'Total da compra: R$ {total:.2f}')