"""
3.Escreva um programa que leia um número, calcule e
imprima a tabuada deste número (de 1 à 10)

"""

n = int(input('Digite um número: '))

inicio = 1 # variável de controle
final = 10

while inicio <= final:
    x = n * inicio
    print(f'{n} x {inicio} = {x}')

    inicio = inicio + 1

    
    