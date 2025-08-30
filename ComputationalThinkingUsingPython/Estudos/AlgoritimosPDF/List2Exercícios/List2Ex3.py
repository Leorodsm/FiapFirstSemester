"""
Escreva um programa que leia um conjunto de 10 números inteiros positivos. Seu programa deve determinar
e imprimir o maior deles. Use o laço FOR.

"""

maior_numero = 0

for i in range (10):
    numero = int(input('Digite um número: '))    
    
    if numero >= maior_numero: 
        maior_numero = numero

print(f'O maior número no conjunto de números digitados é {maior_numero}')


    
        