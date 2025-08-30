"""
Leia 3 números decimais A, B e C e efetue o cálculo das raízes da equação de Bhaskara.
          −𝐵 ± √𝐵2 − 4 ∗ 𝐴 ∗ 𝐶
                 2 ∗ 𝐴
Se não for possível calcular as raízes, ou seja, caso haja uma divisão por 0 ou raiz de número negativo, mostre
a mensagem correspondente “Impossível calcular”.

"""

import math

a = float(input('Digite um número'))
b = float(input('Digite outro número'))
c = float(input('Digite mais um número'))

delta = math.sqrt(b**2-4*a*c)

if a == 0 or delta < 0:
    print('Impossível calcular.')
else:
    x1 = (-b + delta)  / (2 * a)
    x2 = (-b - delta)  / (2 * a)

    print(f'Os valores da equação são\nX1 = {x1} \nX2 = {x2}')
