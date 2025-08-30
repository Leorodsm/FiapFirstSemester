"""
Faça um programa para ler e escrever dados de uma turma de 5 alunos. O programa deve pedir dados como
nome, idade e sexo. O programa deve imprimir os dados do aluno mais velho. Use o laço DO-WHILE.

"""

contador = 1

nome_ = ''
sexo_ = ''
idade_ = 0

while contador <= 5:
    nome = (input('Digite seu nome: '))
    sexo = (input('Digite seu sexo: '))
    idade = int(input('Digite sua idade: '))

    if idade > idade_:
        idade_ = idade
        nome_ = nome
        sexo_ = sexo

    contador = contador + 1

print(f"Aluno mais velho:\nNome:{nome_}\nSexo{sexo_}\nIdade{idade_}")






