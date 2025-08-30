"""
Crie um programa que leia cinco nomes e exiba a quantidade de
nomes que começam com vogal, além de listá-los numerados.

"""

nomes = []

for _ in range(5):
    nome = input("Digite um nome: ")

    nomes.append(nome)

posicao = 0

for atual in nomes:
    posicao += 1

    if atual[0] == "A" or atual[0] == "E" or atual[0] == "I" or atual[0] == "O" or atual[0] == "U":
        print(f"O nome ({atual}) nº{posicao}, começa com vogal")
