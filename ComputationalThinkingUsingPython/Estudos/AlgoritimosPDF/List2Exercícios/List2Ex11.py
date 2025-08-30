"""
Faça um programa que leia um número natural N e calcule a soma abaixo (lembre-se de que tanto as divisões
quanto o resultado devem ser decimais). Utilize o laço que lhe for mais conveniente.

"""

"""
1, -2, +3, -4, +5

8-6 = 2

soma += (1 / contador)

"""

n = 5
i = 1
soma = 0

while i <= n:    
    soma += (1 / i)
    i += 1
    
    if i <= n:
        soma += (1 / -i)
        i += 1

print(soma)