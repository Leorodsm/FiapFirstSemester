total = 0
preco = 0

while preco != -1:
    total += preco
    preco = float(input('\nPreço do item: '))
    print(f'\nTotal da compra: R$ {total:.2f}')

    