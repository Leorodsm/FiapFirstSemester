"""
Calcular e mostrar a média aritmética dos números pares compreendidos entre 13 e 73. Utilize o laço que
lhe for mais conveniente.

"""

contador = 0
soma = 0

for i in range (13,74): 

    if (i % 2) == 0:
        soma += i    
        contador += 1        

media = soma / contador

print(contador)

print(f'A média aritmética dos números pares compreendidos entre 13 e 73 é {media}')














# total = 0
# m = 0

# for i in range(13,74):
#     if (i % 2) == 0:
#         total = total + i
#         m = i + 1    

# media = total / m

# print(f"O resultado disso é: {media}")



