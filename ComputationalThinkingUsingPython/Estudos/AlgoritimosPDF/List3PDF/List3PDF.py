"""
Ao trabalharmos com soluções para
problemas mais complexos, é frequente a
necessidade de manipulação de grandes
quantidades de dados (armazenamento e
acesso aos dados)…

///////////////// Sequências /////////////////

• Variável com diversos compartimentos
• chamados itens da sequência (elementos)
• Noção de ordem entre os itens (1o, 2o, 3o…)
• Cade item é identificado dois valores: nome da variável à qual a sequência
foi atribuída e um número inteiro referente à sua posição na sequência
(índice)
• índices de uma sequência iniciam em 0 (zero)
• Tamanho da sequência é determinado pelo número de elementos da
sequência

///////////////// Funções dentro das Sequências /////////////////


///////////////// len()
A função len() recebe como argumento uma sequência e devolve um número inteiro indicando o tamanho desta sequência.

*Se for uma lista de vários itens, é retornado a quantidade de itens na lista

///////////////// nome_da_sequencia[posicao] -> 
Acessa a primeira posição de uma sequencia
Ex: endereco[0] - Acessa a primeira posição da Lista

LEMBRE-SE. Uma lista sempre começa do zero, então a 3º posição na verdade é: endereco(2)

///////////////// nome_da_sequencia[posicao] = 'Valor para substituir'
Acessa uma posição, e indica o valor que você quer substituir nessa posição

endereco = ['Freguesia','Pirituba','Lapa']
endereco[3] = 'São Bernardo'

print(endereco) 

Freguesia
São Bernardo
Lapa


///////////////// Principais Sequências /////////////////

///////////////// Strings

listas (list)               lista  = []
- grupo = list()

///////////////// Tuplas - Imutáveis e Heterogêneas
Podem ser definidas de várias formas:
• ( ) (tupla vazia)
• (2, ) - vírgula a direita indica uma tupla de apenas um item
• (4, True, 1.5) - itens separados por vírgula

duplas (tuple)              tupla  = ()
- grupo = tupla ()




caracteres (strings)        string = ['']  *O uso de aspas simples/duplas define 
- grupo = ['Adoro python!']



// Range - Imutável e heterogêneo

intervalos (range)          range  = ()
- grupo = range ()

Range, gera um intevalo de números inteiros, e é usado principalmente para o laço "FOR"
- Range (inicio,fim,passos) - Ex: Range(1,10,2) "Inicia no 1, vai até o 10 de 2 em 2. 1, 3, 5, 7..."
ou
- Range (inicio,fim) - Ex: Range(1,10) "Os passos das posições automaticamente vão de 1 em 1.  1, 2, 3, 4, 5"



//// Sequencias Mutáveis e Imutáveis

Mutáveis: Pode ter os valores sobreescritos
Imutáveis: Os valores não podem ser modificados


//// Sequências Homogêneas e Heterogêneas

- homogêneas • todos os itens devem ser do mesmo tipo de variável
- heterogêneas • os itens podem ser de tipos distintos de variáveis

O que define se é alterável ou não?

- O tipo 'List' é mutável e heterogêneo
Podem ser definidas de várias formas: 
• [ ] (lista vazia) 
• [2, True, 1.5] - itens separados por vírgulas



"""

""" ///////////////// Sem uso de lista"""

soma = 0
salario_0 = float(input('Salário: R$ '))
soma += salario_0
salario_1 = float(input('Salário: R$ '))
soma += salario_1
salario_2 = float(input('Salário: R$ '))
soma += salario_2
salario_3 = float(input('Salário: R$ '))
soma += salario_3

media = soma / 4

if salario_0 < media:
    print(f'Abaixo da média: R$ {salario_0:.2f}')
if salario_1 < media:
    print(f'Abaixo da média: R$ {salario_1:.2f}')
if salario_2 < media:
    print(f'Abaixo da média: R$ {salario_2:.2f}')
if salario_3 < media:
    print(f'Abaixo da média: R$ {salario_3:.2f}')


""" ///////////////// Usando Lista"""

salarios = [0, 0, 0, 0]
soma = 0

salarios[0] = float(input('Salário: R$ '))
soma += salarios[0]
salarios[1] = float(input('Salário: R$ '))
soma += salarios[1]
salarios[2] = float(input('Salário: R$ '))
soma += salarios[2]
salarios[3] = float(input('Salário: R$ '))
soma += salarios[3]

media = soma / 4

if salarios[0] < media:
    print(f'Abaixo da média: R$ {salarios[0]:.2f}')
if salarios[1] < media:
    print(f'Abaixo da média: R$ {salarios[1]:.2f}')
if salarios[2] < media:
    print(f'Abaixo da média: R$ {salarios[2]:.2f}')
if salarios[3] < media:
    print(f'Abaixo da média: R$ {salarios[3]:.2f}')


""" ///////////////// Usando Lista e Laço de Repetição """

salarios = [0, 0, 0, 0]
soma = 0
i = 0  # variável que será usada como índice/contador

while i < 4:
    salarios[i] = float(input('Salário: R$ '))
    soma += salarios[i]
    i += 1

media = soma / 4
i = 0  # variável que será usada como índice/contador

while i < 4:
    if salarios[i] < media:
        print(f'Abaixo da média: R$ {salarios[i]:.2f}')
    i += 1


""" ///////////////// Estrutura do Laço FOR """

"""
Python tem uma estrutura de repetição com
quantidade de repetições definida, a estrutura
for (normalmente utilizada quando sabemos
antecipadamente a quantidade de vezes que
o bloco de código deve ser repetido)

"""

"""
• Conhecido como for each (“para cada”) e podemos interpretar como “para
cada item da sequência, faça…”

Sintaxe:

    for <variável> in sequência:
        <bloco de código>

Estrutura do for:
• <variável> é uma variável de controle que, caso não exista precisamente,
será criada no inicio da execução do laço.
• <sequência> sequência de qualquer tipo de tamanho, até mesmo vazia


"""

# Crie um programa que solicite os salários de 4 pessoas, calcule a
# média salarial e exiba os salários abaixo da média.

salarios = []
soma = 0
# O caractere _ (sublinhado) em Python, quando usado como variável em um for, 
# significa apenas que o valor da variável de iteração não será usado dentro do loop.
for _ in range(4):  
    salario = float(input('Salário: R$ '))
    soma += salario
    salarios.append(salario)

media = soma / 4

for salario in salarios:
    if salario < media:
        print(f'Abaixo da média: R$ {salario:.2f}')

# Crie um programa que exiba o alfabeto minúsculo e maiúsculo.
    for letra in 'abcdefghijklmnopqrstuvwxyz':
        print(letra)
    print()
    for letra in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        print(letra)

# Crie um programa que exiba, em ordem crescente, os pares de 10 até 100
# e, em ordem decrescente, os ímpares de 99 até 11.
    for par in range(10, 101, 2):
        print(par, end=' ')
    print()
    for impar in range(99, 10, -2):
        print(impar, end=' ')


# Crie um programa que exiba os sete dias da semana.
    dias = ('domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado')
    for dia in dias:
        print(dia)

# Crie um programa que leia cinco nomes e exiba a quantidade de
# nomes que começam com vogal, além de listá-los numerados.

    nomes = []
    for _ in range(5):
        nomes.append(input('Nome: '))

    qtd = 0
    nomes_com_vogal = []

    for nome in nomes:
        if nome and nome[0].upper() in 'AEIOU':
            qtd += 1
            nomes_com_vogal.append(nome)

    print(f'\n{qtd} dos nomes começam com vogal')
    for i, nome in enumerate(nomes_com_vogal, start=1):
        print(f'{i}º {nome}')



