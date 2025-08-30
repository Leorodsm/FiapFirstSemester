"""
Faça um programa que leia um número N do usuário, some todos os números inteiros de 1 a N, e mostre o
resultado obtido. Use o laço WHILE.

"""

n = float(input("Digite um número: "))

inicio = 1
contador = 0
soma = 0

while contador <= n:
    contador = contador + 1
    soma = soma + contador

    print(f"Soma º{contador}: {soma}")

print(f"\nSoma final: {soma}")
