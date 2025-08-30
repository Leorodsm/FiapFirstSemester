
"""
Fazer um algoritmo que leia três números e imprime a divisão do maior pelo menor.

"""
# Entrada
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

# Processamento

maior = n1

if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

menor = n1

if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

div = maior / menor

print(f'O valor da divisão é: {div}')


    




