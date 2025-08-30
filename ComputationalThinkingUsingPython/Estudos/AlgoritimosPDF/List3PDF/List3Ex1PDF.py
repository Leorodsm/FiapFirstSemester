"""
Crie um programa que solicite os salários de 4 pessoas, calcule a média salarial e exiba os salários abaixo da média.

"""
salarios = []
soma_salarios = 0

for _ in range(4):
    salario_digitado = float(input('Digite um salário: R$'))
    soma_salarios = soma_salarios + salario_digitado

    salarios.append(salario_digitado)

media_salarial = soma_salarios / 4
posicao = 0

for salario_da_lista in salarios:
    posicao = posicao + 1

    if salario_da_lista < media_salarial:
        print(f'Salário nº{posicao} abaixo da média. Média: R$ {media_salarial}, Salário: R${salario_da_lista}')

