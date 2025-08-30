""" ___________________________________________________________________________________________________________________________________
8 - Um algorintmo que leia dois números e verifique se os números são iguais a zero. Caso sejam, o algoritmo deve solicitar novamente os
números. Caso sejam diferentes de zero, o algoritmo deve somar os números e dividi-los por dois e apresentar o resultado.

(Entrada)
- 

(Processamento)
- 

(Saída)
- 

"""

print('\nAlgorítimo: Média de números (Diferentes de 0)\n')

n1 = float(input('Digite um múmero: '))
n2 = float(input('Digite outro número: '))

if n1 != 0 and n2 != 0:
    m = (n1 + n2) / 2
    print(f'\n- A média entre {n1:.1f} e {n2:.1f} é: {m:.1f}\n')
else:
    print(f'\n- Não se pode fazer média com número 0 nesse algorítimo.\n')


























"""
# Entrada
print('\nAlgorítimo: Média entre dois números, negando qualquer número nulo\n')

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
           
# Processamento
if n1 == 0 or n2 == 0:
    print('\nNúmeros iguais a 0 não podem serem inseridos nesse calculo. Inicialize o programa novamente e tente novamente.\n')
else:
    media = (n1+n2)/2
    print(f'\nA média entre {n1} e {n2} é: {media}\n')
"""