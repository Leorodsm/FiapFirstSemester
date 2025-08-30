"""
Fazer um algoritmo que leia os dois lados A e B de um triângulo retângulo e calcula a hipotenusa do triângulo.
Para esse caso, considere que ℎ𝑖𝑝𝑜𝑡𝑒𝑛𝑢𝑠𝑎 = √𝐴 2 + 𝐵 2 . Dica: nesse programa, você deve usar a
função matemática Math.sqrt(). Por exemplo, a raiz de 121 ficaria Math.sqrt(121).

"""

import math

a = float(input("Digite um lado: "))
b = float(input("Digite outro lado: "))

hipotenusa = math.sqrt(a**2 + b**2)

print(f'O valor da hipotenusa é: {hipotenusa}')