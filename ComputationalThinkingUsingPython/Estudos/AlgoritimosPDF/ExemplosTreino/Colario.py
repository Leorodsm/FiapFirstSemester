"""Usando if:"""

x = 10
if x == 1:
    print("Um")
elif x == 2:
    print("Dois")
elif x == 3:
    print("Três")
else:
    print("Outro valor")

"""Usando match:"""

x = 10
match x:
    case 1:
        print("Um")
    case 2:
        print("Dois")
    case 3:
        print("Três")
    case _:
        print("Outro valor")





'''
Escreva um programa em Python que simule uma calculadora simples, contendo
as quatro operações básicas (+, -, *, / - acrescente mais uma operação). 

O programa deve ter:
- Menu de operações
- Realizar o calculo escolhido (dois números)
- Apresentar o resultado
'''

print('\n**- Calculadora Simples -**')
print('---------------------------\n')

print('1 - Adição')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')
print('5 - Potência')

op = int(input('Operação: '))
n1 = float(input('Número: '))
n2 = float(input('Número: '))

match op:
    case 1:
        print(f'Resultado: {n1+n2}')
    case 2:
        print(f'Resultado: {n1-n2}')
    case 3:
        print(f'Resultado: {n1*n2}')
    case 4:
        if n2!=0:
            print(f'Resultado: {n1/n2}')
        else:
            print('divisão por zero!')    
    case 5:
        print(f'Resultado: {n1**n2}')
    case _:
        print('Operação inválida!')