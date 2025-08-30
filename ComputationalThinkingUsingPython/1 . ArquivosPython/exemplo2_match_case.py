print('Exemplo com if-elif-else')
print('------------------------')

final_placa = int(input('Número: '))

if final_placa == 1 or final_placa == 2:
    print('Segunda-feira')
elif final_placa == 3 or final_placa == 4:
    print('Terça-feira')
elif final_placa == 5 or final_placa == 6:
    print('Quarta-feira')
elif final_placa == 7 or final_placa == 8:
    print('Quinta-feira')
elif final_placa == 9 or final_placa == 0:
    print('Sexta-feira')
else:
    print('número inválido')

print('\nExemplo com match-case')
print('------------------------')
final_placa = int(input('Número: '))

match final_placa:
    case 1|2:
        print('Segunda-feira')
    case 3|4:
        print('Terça-feira')
    case 5|6:
        print('Quarta-feira')
    case 7|8:
        print('Quinta-feira')
    case 9|0:
        print('Sexta-feira')
    case _:
        print('número inválido')



'''
Escreva um programa em Python que leia o nome de um aluno e 3 notas. O
programa deve calcular a média e verificar se o aluno está aprovado ou
reprovado. Para estar aprovado, o aluno deve ter média maior ou igual a 6.
Além'disso, o programa deve determinar o conceito obtido pelo aluno, de acordo
com a tabela abaixo:

Conceito 'A' - media >= 9 E media <= 10
Conceito 'B' - media >= 8 E media < 9
Conceito 'C' - media >= 7 E media < 8
Conceito 'D' - media >= 6 E media < 7
Conceito 'E' - media < 6

O programa deve imprimir o nome do aluno, a média, o status e o
conceito obtido - match_case (de acordo com o conceito)

'''

nome = input('Nome: ')

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
n3 = float(input('Nota 3: '))

media = (n1+n2+n3)/3

if media >= 9 and media <=10:
    status = 'aprovado'
    conceito = 'A'
elif media >= 8 and media < 9:
    status = 'aprovado'
    conceito = 'B'
elif media >= 7 and media < 8:
    status = 'aprovado'
    conceito = 'C'
elif media >= 6 and media < 7:
    status = 'aprovado'
    conceito = 'D'
else:
    status = 'reprovado'
    conceito = 'E'

match conceito:
    case 'A':
        print(f'Nome: {nome}, você foi {status} com conceito {conceito} \n Média: {media:.1f}')
    case 'B':
        print(f'Nome: {nome}, você foi {status} com conceito {conceito} \n Média: {media:.1f}')
    case 'C':
        print(f'Nome: {nome}, você foi {status} com conceito {conceito} \n Média: {media:.1f}')
    case 'D':
        print(f'Nome: {nome}, você foi {status} com conceito {conceito} \n Média: {media:.1f}')
    case 'E':
        print(f'Nome: {nome}, você foi {status} com conceito {conceito} \n Média: {media}')












        
        






