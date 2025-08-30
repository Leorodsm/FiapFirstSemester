"""
Faça um programa que calcule e imprima o resultado da soma abaixo (lembre-se de que tanto as divisões
quanto o resultado devem ser decimais). Utilize o laço que lhe for mais conveniente.

"""

contador = 1
soma = 0

while contador <= 20:
    soma += 1 / contador

    contador += 1

print(f"O resultado é: {soma:.4f}")